from rest_framework import serializers

from tasks.models import Team, Task, StatusChoices
from users.models import User, UserChoices, TeamUser, TaskUser
from users.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    """."""

    status_display = serializers.CharField(source="get_status_display", read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    status = serializers.CharField(required=False)
    allotted_members = serializers.ListField(child=serializers.IntegerField(), required=False)
    members = serializers.SerializerMethodField()
    team_name = serializers.CharField(read_only=True, source="team.name")

    def get_members(self, task):
        """."""

        return [UserSerializer(item.user).data for item in task.task_users.all()]

    def validate(self, attrs):
        """."""

        if "status" in attrs and attrs.get("status") not in StatusChoices.values:
            status = attrs.get('status')
            raise serializers.ValidationError(detail={"status": f"{status} is not a valid choice"})
        return super(TaskSerializer, self).validate(attrs)

    def create(self, validated_data):
        """."""

        if "allotted_members" in validated_data:
            validated_data.pop("allotted_members")
        task = Task.objects.create(**validated_data)
        return task

    def update(self, instance, validated_data):
        """."""

        request = self.context.get("request")
        team_users = [team_user.user for team_user in instance.team.team_users.all()]
        if request.user not in team_users:
            raise serializers.ValidationError(detail={"member": "You are not a member of this team"})
        task_users = [task_user.user for task_user in instance.task_users.all()]
        if request.user.role != UserChoices.LEADER and request.user not in task_users:
            raise serializers.ValidationError(detail={"member": "You are not a member of this task"})
        if request.user.role == UserChoices.MEMBER and \
                (len(validated_data) > 1 or not validated_data.get("status") or "allotted_members" in validated_data):
            raise serializers.ValidationError(detail={"member": "Members can only update status"})
        if "allotted_members" in validated_data:
            if request.user.role != UserChoices.LEADER:
                raise serializers.ValidationError(detail={"leader": "Only leader can allot tasks"})
            members = validated_data.pop("allotted_members")
            member_objs = []
            for member_id in members:
                if not User.objects.filter(pk=member_id):
                    raise serializers.ValidationError(detail={"member": f"Member with id {member_id} does not exist"})
                user = User.objects.get(pk=member_id)
                if user not in team_users:
                    raise serializers.ValidationError(detail={"member": f"Member with id {member_id} is not a member of this team."})
                if user in task_users:
                    raise serializers.ValidationError(detail={"member": f"Member with id {member_id} has already been allotted this task."})
                if user.role != UserChoices.MEMBER:
                    raise serializers.ValidationError(detail={"member": f"User with id {user.id} is not a member"})
                member_objs.append(user)
            task_users = [TaskUser(task=instance, user=user) for user in member_objs]
            TaskUser.objects.bulk_create(task_users)
        return super(TaskSerializer, self).update(instance, validated_data)

    class Meta:
        """."""

        model = Task
        fields = [
            'id',
            'name',
            'created_at',
            'updated_at',
            'completed_at',
            'status',
            'team',
            'team_name',
            'status_display',
            'allotted_members',
            'members',
        ]


class TeamSerializer(serializers.ModelSerializer):
    """."""

    members = serializers.SerializerMethodField()
    tasks = TaskSerializer(many=True, read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def get_members(self, team: Team):
        """."""

        return [UserSerializer(item.user).data for item in team.team_users.all()]

    class Meta:
        """."""

        model = Team
        fields = [
            'id',
            'name',
            'members',
            'tasks',
            'created_at',
            'updated_at',
        ]


class TeamCreateSerializer(serializers.Serializer):
    """."""

    team = serializers.CharField(max_length=50)
    leader = serializers.IntegerField()
    members = serializers.ListField(child=serializers.IntegerField())

    def validate(self, attrs):
        """."""

        team = attrs.get("team")
        leader = attrs.get('leader')
        members = attrs.get('members')
        if not isinstance(team, str):
            raise serializers.ValidationError(detail={"name": "Team name must be a string"})
        try:
            int(team)
            raise serializers.ValidationError(detail={"name": "Team name must be a string"})
        except ValueError:
            pass
        if Team.objects.filter(name=team):
            raise serializers.ValidationError(detail={"name": "Team with this name already exists"})
        if not User.objects.filter(pk=leader):
            raise serializers.ValidationError(detail={"leader": f"Leader with id {attrs.get('leader')} does not exist"})
        user = User.objects.get(pk=leader)
        if user.role != UserChoices.LEADER:
            raise serializers.ValidationError(detail={"leader": f"User with id {user.id} is not a leader"})
        for member_id in members:
            if not User.objects.filter(pk=member_id):
                raise serializers.ValidationError(detail={"member": f"Member with id {member_id} does not exist"})
            user = User.objects.get(pk=member_id)
            if user.role != UserChoices.MEMBER:
                raise serializers.ValidationError(detail={"member": f"User with id {user.id} is not a member"})
        return attrs

    def create(self, validated_data):
        """."""

        team = validated_data.get("team")
        leader = validated_data.get("leader")
        members = validated_data.get("members")
        team = Team.objects.create(name=team)
        users = [User.objects.get(pk=leader)] \
                + [User.objects.get(pk=member) for member in members]
        team_users = [TeamUser(team=team, user=user) for user in users]
        TeamUser.objects.bulk_create(team_users)
        return team

from rest_framework import views, viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from tasks.filters import TeamFilterSet, TaskFilterSet
from tasks.models import Task, Team
from tasks.pagination import TaskPagination, TeamPagination
from tasks.permissions import IsUser, IsMember, IsLeader
from tasks.serializers import TeamSerializer, TeamCreateSerializer, TaskSerializer


class TeamListView(generics.ListAPIView):
    """."""

    queryset = Team.objects.prefetch_related('tasks', 'team_users__user').all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = TeamPagination
    filterset_class = TeamFilterSet


class TeamCreateView(views.APIView):
    """."""

    serializer_class = TeamCreateSerializer
    permission_classes = [IsUser]

    def post(self, request, *args, **kwargs):
        """."""

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        team = serializer.save()
        team_details = TeamSerializer(team)
        return Response(team_details.data)


class TaskViewSet(viewsets.ModelViewSet):
    """."""

    queryset = Task.objects.prefetch_related('task_users__user', 'team__team_users__user').all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination
    filterset_class = TaskFilterSet

    def get_permissions(self):
        """."""

        if self.request.method == 'POST':
            permissions = [IsUser]
        elif self.request.method in ['PATCH', 'PUT']:
            permissions = [IsMember | IsLeader]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

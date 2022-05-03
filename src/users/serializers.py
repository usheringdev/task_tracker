from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """."""

    role_display = serializers.CharField(source="get_role_display", read_only=True)

    class Meta:
        """."""

        model = User
        fields = [
            'id',
            'username',
            'created_at',
            'updated_at',
            'first_name',
            'last_name',
            'role',
            'role_display',
        ]

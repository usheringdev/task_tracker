from rest_framework import permissions

from users.models import UserChoices


class PermissionMixin:
    """."""

    curr_role = None

    def has_permission(self, request, view):
        """."""

        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role == self.curr_role


class IsUser(PermissionMixin, permissions.BasePermission):
    """."""

    curr_role = UserChoices.USER


class IsMember(PermissionMixin, permissions.BasePermission):
    """."""

    curr_role = UserChoices.MEMBER


class IsLeader(PermissionMixin, permissions.BasePermission):
    """."""

    curr_role = UserChoices.LEADER

from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
from django.db import models

from tasks.models import Team, Task


class UserChoices(models.TextChoices):
    """."""

    USER = "user", _("User")
    MEMBER = "member", _("Member")
    LEADER = "leader", _("Leader")


class User(AbstractUser):
    """."""

    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    username = models.EmailField(unique=True)
    role = models.CharField(
        max_length=10,
        choices=UserChoices.choices,
        default=UserChoices.USER
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "username"

    objects = UserManager()

    def __str__(self):
        """."""

        return self.username

    class Meta:
        """."""

        ordering = ['-updated_at']


class TaskUser(models.Model):
    """."""

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_users')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_users')

    class Meta:
        """."""

        unique_together = ['task', 'user']


class TeamUser(models.Model):
    """."""

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_users')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_users')

    class Meta:
        """."""

        unique_together = ['team', 'user']
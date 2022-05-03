from django.db import models
from django.utils.translation import gettext_lazy as _


class StatusChoices(models.TextChoices):
    """."""

    ASSIGNED = "assigned", _("Assigned")
    IN_PROGRESS = "in progress", _("In Progress")
    UNDER_REVIEW = "under review", _("Under Review")
    DONE = "done", _("Done")


class Team(models.Model):
    """."""

    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """."""

        return self.name

    class Meta:
        """."""

        ordering = ['-updated_at']


class Task(models.Model):
    """."""

    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='tasks',
    )
    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
        default=StatusChoices.ASSIGNED,
    )
    mail_sent = models.BooleanField(default=False)

    def __str__(self):
        """."""

        return self.name

    class Meta:
        """."""

        ordering = ['-updated_at']

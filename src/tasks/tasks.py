from celery import shared_task
from django.core.mail import send_mail

from tasks.models import Task
from users.models import UserChoices


@shared_task
def send_task_creation_mail_to_leader():
    """."""

    tasks = Task.objects.prefetch_related('team__team_users__user').filter(mail_sent=False)
    for task in tasks:
        team_leader = task.team.team_users.filter(user__role=UserChoices.LEADER).first()
        send_mail(
            "New Task assigned to your team",
            f"Task with id {task.id} created. Please assign it to your team member(s)",
            "test@task.app",
            [team_leader.user.username],
        )
    tasks.update(mail_sent=True)

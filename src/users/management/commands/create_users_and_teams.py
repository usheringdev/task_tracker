from django.core.management.base import BaseCommand

from tasks.models import Team
from users.models import UserChoices, User


class Command(BaseCommand):
    """."""

    help = 'Create teams, users, team members and team leaders'

    def handle(self, *args, **options):
        """."""

        # Users

        User.objects.create_user(
            username='user.one@mail.com',
            first_name='User',
            last_name='One',
            password='user@one',
            role=UserChoices.USER
        )

        User.objects.create_user(
            username='user.two@mail.com',
            first_name='User',
            last_name='Two',
            password='user@two',
            role=UserChoices.USER
        )

        User.objects.create_user(
            username='user.three@mail.com',
            first_name='User',
            last_name='Three',
            password='user@three',
            role=UserChoices.USER
        )

        # Members

        User.objects.create_user(
            username='member.one@mail.com',
            first_name='Member',
            last_name='One',
            password='member@one',
            role=UserChoices.MEMBER,
        )

        User.objects.create_user(
            username='member.two@mail.com',
            first_name='Member',
            last_name='Two',
            password='member@two',
            role=UserChoices.MEMBER,
        )

        User.objects.create_user(
            username='member.three@mail.com',
            first_name='Member',
            last_name='Three',
            password='member@three',
            role=UserChoices.MEMBER,
        )

        User.objects.create_user(
            username='member.four@mail.com',
            first_name='Member',
            last_name='Four',
            password='member@four',
            role=UserChoices.MEMBER,
        )

        User.objects.create_user(
            username='member.five@mail.com',
            first_name='Member',
            last_name='Five',
            password='member@five',
            role=UserChoices.MEMBER,
        )

        User.objects.create_user(
            username='member.six@mail.com',
            first_name='Member',
            last_name='Six',
            password='member@six',
            role=UserChoices.MEMBER,
        )

        # Leaders

        User.objects.create_user(
            username='leader.one@mail.com',
            first_name='Leader',
            last_name='One',
            password='leader@one',
            role=UserChoices.LEADER,
        )

        User.objects.create_user(
            username='leader.two@mail.com',
            first_name='Leader',
            last_name='Two',
            password='leader@two',
            role=UserChoices.LEADER,
        )

        User.objects.create_user(
            username='leader.three@mail.com',
            first_name='Leader',
            last_name='Three',
            password='leader@three',
            role=UserChoices.LEADER,
        )

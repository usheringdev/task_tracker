from django_filters import rest_framework as filters

from users.models import User, UserChoices


class UserFilterSet(filters.FilterSet):
    """."""

    role = filters.ChoiceFilter(choices=UserChoices.choices)

    class Meta:
        """."""

        model = User
        fields = {
            "first_name": ["icontains"],
            "last_name": ["icontains"],
            "username": ["icontains"],
        }

from django_filters import rest_framework as filters

from tasks.models import Team, Task, StatusChoices


class TeamFilterSet(filters.FilterSet):
    """."""

    class Meta:
        """."""

        model = Team
        fields = {
            "name": ["icontains"],
        }


class TaskFilterSet(filters.FilterSet):
    """."""

    status = filters.ChoiceFilter(choices=StatusChoices.choices)

    class Meta:
        """."""

        model = Task
        fields = {
            "name": ["icontains"],
            "team__name": ["icontains"],
        }

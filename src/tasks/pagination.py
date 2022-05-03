from rest_framework import pagination


class TaskPagination(pagination.PageNumberPagination):
    """."""

    page_size = 10


class TeamPagination(pagination.PageNumberPagination):
    """."""

    page_size = 10

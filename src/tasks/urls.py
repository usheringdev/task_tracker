from django.urls import path
from rest_framework.routers import DefaultRouter

from tasks.views import TeamCreateView, TaskViewSet, TeamListView

router = DefaultRouter()
router.register("tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    path('teams/', TeamCreateView.as_view(), name="team-create"),
    path('teams_list/', TeamListView.as_view(), name="team-list"),
] + router.urls

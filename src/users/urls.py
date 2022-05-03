from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users.views import LogOutView, ListUsersAPIView

urlpatterns = [
    path('log_in/', obtain_auth_token, name="log-in"),
    path('log_out/', LogOutView.as_view(), name="log-out"),
    path('users_list/', ListUsersAPIView.as_view(), name="users-list"),
]

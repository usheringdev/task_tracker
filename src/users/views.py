from rest_framework import views, status, generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.filters import UserFilterSet
from users.models import User
from users.pagination import UserPagination
from users.serializers import UserSerializer


class LogOutView(views.APIView):
    """."""

    def post(self, request, *args, **kwargs):
        """."""

        Token.objects.filter(user=self.request.user).delete()
        return Response("You have logged out successfully", status=status.HTTP_204_NO_CONTENT)


class ListUsersAPIView(generics.ListAPIView):
    """."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = UserPagination
    filterset_class = UserFilterSet

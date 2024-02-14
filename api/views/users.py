from django.contrib.auth.models import User
from api.serializers import UserSerializer
from .authenticated import AuthenticatedViewSet


class UserViewSet(AuthenticatedViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

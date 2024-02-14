from django.contrib.auth.models import Group
from api.serializers import GroupSerializer
from .authenticated import AuthenticatedViewSet


class GroupViewSet(AuthenticatedViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


from django.contrib.auth.models import Group
from api.serializers import GroupSerializer
from djangoProject.common.authenticated_view_set import AuthenticatedViewSet


class GroupViewSet(AuthenticatedViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


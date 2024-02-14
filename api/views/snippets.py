from api.models import Snippet
from api.serializers import SnippetSerializer
from .authenticated import AuthenticatedViewSet


class SnippetsViewSet(AuthenticatedViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

from api.models import Snippet
from api.serializers import SnippetSerializer
from djangoProject.common.authenticated_view_set import AuthenticatedViewSet


class SnippetsViewSet(AuthenticatedViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

from rest_framework.views import APIView
from rest_framework import permissions


class AuthenticatedView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated]

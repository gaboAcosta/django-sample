from django.urls import include, path
from rest_framework import routers

from api.views import GroupViewSet, UserViewSet, SnippetsViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'snippets', SnippetsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += router.urls

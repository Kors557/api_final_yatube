from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from django.urls import include, path

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = SimpleRouter()

router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
app_name = 'api'

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]

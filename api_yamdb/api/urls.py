from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    APISignUp, APIToken, CommentViewSet, ReviewViewSet, UserViewSet
)

router_v1 = DefaultRouter()

router_v1.register('users', UserViewSet)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='reviews'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'
    r'/comments', CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/auth/signup/', APISignUp.as_view(),
         name='get_confirmation_code'),
    path('v1/auth/token/', APIToken.as_view(), name='get_jwt_token'),
    path('v1/', include(router_v1.urls))
]

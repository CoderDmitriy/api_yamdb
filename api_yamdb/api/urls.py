from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    APISignUp, APIToken, CommentViewSet, ReviewViewSet, UserViewSet, CategoryViewSet, GenreViewSet, TitleViewSet
)

router = DefaultRouter()

router.register('users', UserViewSet)
router.register(r'titles/(?P<title_id>\d+)/reviews',
                   ReviewViewSet, basename='reviews')
router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'
                   r'/comments', CommentViewSet, basename='comments')
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'titles', TitleViewSet)
urlpatterns = [
    path('v1/auth/signup/', APISignUp.as_view(),
         name='get_confirmation_code'),
    path('v1/auth/token/', APIToken.as_view(), name='get_jwt_token'),
    path('v1/', include(router.urls))
]

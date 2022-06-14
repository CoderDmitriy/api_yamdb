from django.urls import include, path

from .views import UserViewSet, APIToken, APISignUp
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('users', UserViewSet)

urlpatterns = [
    path('v1/auth/signup/', APISignUp.as_view(),
         name='get_confirmation_code'),
    path('v1/auth/token/', APIToken.as_view(), name='get_jwt_token'),
    path('v1/', include(router.urls)),
]

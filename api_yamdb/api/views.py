
from django.core.mail import send_mail

from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters, permissions, viewsets

from reviews.models import User

from .serializer import UserSerializers, UserMeSerializers
from . permissions import IsAdmin


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAdmin]
    filter_backends = (filters.SearchFilter, )
    search_fields = ('username', )
    lookup_field = 'username'

    @action(
        detail=False, methods=['get', 'patch'],
        url_path='me', url_name='me',
        permission_classes=(permissions.IsAuthenticated,)
    )
    def get_me(self, request):
        serializer = UserMeSerializers(request.user)
        if request.method != 'PATCH':
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = UserMeSerializers(
            request.user, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class APISignUp(APIView):
    def post(self, request):
        pass


class APIToken(APIView):
    def post(self, request):
        pass

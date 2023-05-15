from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

from apps.user.serializers.user import (
    UserSerializer, UserListCreateSerializer, UserAuthSerializer)
from apps.user.utils.filter import UserFilters


class UserViewSet(ModelViewSet):
    """
    CRUD operations for User
    """

    queryset = User.objects.all()
    filterset_class = UserFilters
    search_fields = ('first_name',)
    ordering_fields = ('id', 'username', 'first_name', 'last_name', 'email')
    lookup_url_kwarg = 'user_id'

    def get_serializer_class(self):
        if self.action in ('create', 'list'):
            serializer_class = UserListCreateSerializer
        elif self.action == 'sign_in':
            serializer_class = UserAuthSerializer
        else:
            serializer_class = UserSerializer
        return serializer_class

    @action(detail=False, methods=['post'], url_name='sign_in')
    def sign_in(self, request):
        """Sign In to system"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError, AuthenticationFailed

from apps.user.utils.token import get_tokens


class UserListCreateSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, label="Password")
    password2 = serializers.CharField(write_only=True, label="Password Confirmation")

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        read_only_fields = ('id',)

    def validate(self, attrs):
        """
        Validate input passwords
        """
        password1 = attrs.get('password1')
        password2 = attrs.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError({'message': 'password1 is not equel password2'})
        del attrs['password2']
        return attrs

    def create(self, validated_data):
        """
        Create and return a new "User" instance, given the validated data.
        """
        password = validated_data.pop('password1')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'date_joined')
        read_only_fields = ('id', 'is_active', 'date_joined')
        extra_kwargs = {
            "username": {"required": False}
        }


class UserAuthSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)
    tokens = serializers.JSONField(default=dict, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'tokens')

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        tokens = get_tokens(user)
        return {
            'username': user.username,
            'tokens': tokens
        }

from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth import password_validation
from django.contrib.auth import login

from users.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'uuid',
            'phone',
            'email',
            'first_name',
            'last_name',
            'gender',
            'bio',
            'avatar',
            'is_active',
            'is_staff',
            'created_at',
            'updated_at',
        )


class UserShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'uuid',
            'phone',
        )


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        max_length=50
    )

    class Meta:
        model = CustomUser
        fields = (
            'uuid',
            'phone',
            'password',
            'email',
            'first_name',
            'last_name',
            'gender',
            'bio',
            'avatar',
        )
        read_only_fields = ('created_at', 'updated_at')

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        instance = super().create(validated_data)
        login(self.context['request'], instance)
        return instance


class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'phone',
            'password',
            'email',
            'first_name',
            'last_name',
            'gender',
            'bio',
            'avatar',
        )


class UserLastActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = (
            'last_login',
            'last_activity'
        )

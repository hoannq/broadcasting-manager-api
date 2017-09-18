# -*- coding: utf-8 -*-
__author__ = 'TOANTV'
from rest_framework import serializers

from one_users.models import OneUsers


# Class for admin gets, create user
class OneUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneUsers
        fields = (
            'id', 'username', 'password', 'email', 'fullname', 'is_superuser', 'is_active', 'date_joined', "last_login")
        read_only_fields = ('date_joined', 'last_login', 'id')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = OneUsers(
            **validated_data
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# Class for admin get, update and delete user information
class OneUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneUsers
        fields = (
            'id', 'username', 'email', 'fullname', 'is_superuser', 'is_active', 'date_joined', "last_login")
        read_only_fields = ('date_joined', 'last_login', 'email', 'id')
        extra_kwargs = {'password': {'write_only': True}}


# Serializer for authenticated user
class OneAuthenticatedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneUsers
        fields = ('id', 'username', 'email', 'fullname', 'date_joined', 'last_login', 'is_superuser', 'is_active')
        read_only_fields = ('date_joined', 'last_login', 'email', 'id', 'is_superuser', 'is_active')


# Serializer for set password
class ChangePasswordUserSerializer(serializers.Serializer):
    password = serializers.RegexField(min_length=6, max_length=128,
                                      regex='^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d\~\`\!\@\#\$%\^\&\*\(\)\+\-\_\=\,\;\'\"\[\]\?\<\>\\\.\/\:\{\}\|]{8,}')

    class Meta:
        fields = ('password')
        extra_kwargs = {'password': {'write_only': True}}


class OneUserSerializerEmail(serializers.ModelSerializer):
    class Meta:
        model = OneUsers
        fields = ('fullname', 'email')

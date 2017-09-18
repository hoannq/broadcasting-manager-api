__author__ = 'TOANTV'
from rest_framework.permissions import BasePermission


class IsOneUserAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated()


class IsOneSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsOneSuperAdminOrIsSelf(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_superuser

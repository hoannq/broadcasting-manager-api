# -*- coding: utf-8 -*-
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from rest_framework import filters
from rest_framework import generics
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from one_auth.authentication import OneTokenAuthentication
from one_users.models import OneUsers
from one_users.permissions import IsOneUserAuthenticated, IsOneSuperAdmin
from one_users.serializers import OneAuthenticatedUserSerializer, ChangePasswordUserSerializer
from one_users.serializers import OneUserSerializer, OneUserDetailsSerializer, OneUserSerializerEmail
from broadcasting_manager.views import JSONResponse


class OneUsersList(generics.ListCreateAPIView):
    queryset = OneUsers.objects.filter(~Q(id=2))
    serializer_class = OneUserSerializer
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneSuperAdmin,)
    renderer_classes = (JSONRenderer,)
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend,)
    search_fields = ('username', 'email')
    filter_fields = ('username', 'is_superuser', 'email', 'is_active')


# GET /users/profile/
# PUT /users/profile/
# DELETE /users/profile/
class OneUserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = OneUsers.objects.all()
    serializer_class = OneUserDetailsSerializer
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneSuperAdmin,)
    renderer_classes = (JSONRenderer,)

    def get_object(self):
        return OneUsers.objects.get(pk=self.kwargs['pk'])

    def perform_update(self, serializer):
        serializer.save()
        # Update password
        user = self.get_object()
        if "password" in self.request.data and self.request.data["password"] != "":
            password_serializer = ChangePasswordUserSerializer(data={"password": self.request.data["password"]})
            if password_serializer.is_valid(raise_exception=True):
                # Logout all sessions if new password is not current password
                if not user.check_password(self.request.data["password"]):
                    OneTokenAuthentication().delete_another_tokens(user)
                user.set_password(self.request.data["password"])
                user.save()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_superuser == 1 and OneUsers.objects.filter(is_superuser=1, is_active=1).count() == 1:
            return JSONResponse({'status': 'error',
                                 "error": _(
                                     "You cannot delete last supper user.\nPlease change super user permission to another user.")},
                                status=status.HTTP_400_BAD_REQUEST)
        instance.is_active = 0
        instance.save()
        return JSONResponse({'status': 'success'}, status=status.HTTP_200_OK)


# GET /users/profile/
# PUT /users/profile/
class OneAuthenticatedUserDetail(generics.RetrieveUpdateAPIView):
    queryset = OneUsers.objects.all()
    serializer_class = OneAuthenticatedUserSerializer
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneUserAuthenticated,)
    renderer_classes = (JSONRenderer,)

    def get_object(self):
        return self.request.user


# POST /users/profile/reset_password/
class OneUserSetPassword(generics.CreateAPIView):
    queryset = OneUsers.objects.all()
    serializer_class = ChangePasswordUserSerializer
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneUserAuthenticated,)
    renderer_classes = (JSONRenderer,)

    def create(self, request, *args, **kwargs):
        user = request.user
        request_data = request.data
        if user.check_password(request_data["current-password"]):
            serializer = ChangePasswordUserSerializer(data={"password": self.request.data["new-password"]})
            if serializer.is_valid(raise_exception=True):
                if "new-password" in request_data:
                    user.set_password(request_data["new-password"])
                    user.save()
                    # Logout all sessions
                    if request_data["new-password"] != request_data["current-password"]:
                        OneTokenAuthentication().delete_another_tokens(user)
                    return JSONResponse({'status': 'success'}, status=status.HTTP_200_OK)
        else:
            return JSONResponse({'status': "fail",
                                 'data': {"password": _("Current password is not correct")}},
                                status=status.HTTP_400_BAD_REQUEST)


class OneUsersListEmail(generics.ListCreateAPIView):
    queryset = OneUsers.objects.filter(~Q(id=2), is_active=True)
    serializer_class = OneUserSerializerEmail
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneUserAuthenticated,)
    renderer_classes = (JSONRenderer,)
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend,)
    search_fields = ('username', 'email')
    filter_fields = ('username', 'email')

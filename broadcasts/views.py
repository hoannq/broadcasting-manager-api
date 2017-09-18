# Create your views here.
from rest_framework import generics, filters
from rest_framework.renderers import JSONRenderer

from broadcasts.models import Broadcast
from broadcasts.serializers import BroadcastSerializers
from one_auth.authentication import OneTokenAuthentication
from one_users.permissions import IsOneUserAuthenticated


class BroadcastListView(generics.ListCreateAPIView):
    queryset = Broadcast.objects.all()
    serializer_class = BroadcastSerializers
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneUserAuthenticated,)
    renderer_classes = (JSONRenderer,)
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend,)
    search_fields = ('name',)
    filter_fields = ('name', 'base_station',)


class BroadcastDetails(generics.mixins.RetrieveModelMixin,
                       generics.mixins.UpdateModelMixin,
                       generics.mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    queryset = Broadcast.objects.all()
    serializer_class = BroadcastSerializers
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneUserAuthenticated,)
    renderer_classes = (JSONRenderer,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

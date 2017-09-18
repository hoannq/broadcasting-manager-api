# Create your views here.
# Create your views here.
from rest_framework import generics, filters
from rest_framework.renderers import JSONRenderer

from one_auth.authentication import OneTokenAuthentication
from one_users.permissions import IsOneUserAuthenticated
from timeranges.models import Timerange
from timeranges.serializers import TimerangeSerializers


class TimerangeListView(generics.ListCreateAPIView):
    queryset = Timerange.objects.all()
    serializer_class = TimerangeSerializers
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneUserAuthenticated,)
    renderer_classes = (JSONRenderer,)
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend,)
    search_fields = ('broadcasting_status',)
    filter_fields = ('broadcasting_status',)


class TimerangeDetails(generics.mixins.RetrieveModelMixin,
                       generics.mixins.UpdateModelMixin,
                       generics.mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    queryset = Timerange.objects.all()
    serializer_class = TimerangeSerializers
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneUserAuthenticated,)
    renderer_classes = (JSONRenderer,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

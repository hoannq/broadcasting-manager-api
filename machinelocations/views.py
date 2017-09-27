# Create your views here.
import datetime
import time

from rest_framework import generics, filters, status
from rest_framework.renderers import JSONRenderer

from broadcasting_manager.views import JSONResponse
from machinelocations.serializers import MachinelocationSerializers
from one_auth.authentication import OneTokenAuthentication
from one_users.permissions import IsOneUserAuthenticated
from unitprices.models import Machinelocation


class MachinelocationListView(generics.ListCreateAPIView):
    queryset = Machinelocation.objects.filter(deleted_at=0)
    serializer_class = MachinelocationSerializers
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneUserAuthenticated,)
    renderer_classes = (JSONRenderer,)
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend,)
    search_fields = ('name',)
    filter_fields = ('name',)


class MachinelocationDetails(generics.mixins.RetrieveModelMixin,
                             generics.mixins.UpdateModelMixin,
                             generics.mixins.DestroyModelMixin,
                             generics.GenericAPIView):
    queryset = Machinelocation.objects.filter(deleted_at=0)
    serializer_class = MachinelocationSerializers
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneUserAuthenticated,)
    renderer_classes = (JSONRenderer,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.deleted_at = int(time.mktime(datetime.datetime.now().timetuple()))
        instance.save()
        return JSONResponse({'status': 'success'}, status=status.HTTP_204_NO_CONTENT)

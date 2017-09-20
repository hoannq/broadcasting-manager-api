# Create your views here.
from django.utils.translation import ugettext_lazy as _
from rest_framework import generics, filters, status
from rest_framework.renderers import JSONRenderer

from basestations.models import Basestation
from basestations.serializers import BasestationSerializers
from broadcasting_manager.views import JSONResponse
from broadcasts.models import Broadcast
from one_auth.authentication import OneTokenAuthentication
from one_users.permissions import IsOneUserAuthenticated


class BasestationListView(generics.ListCreateAPIView):
    queryset = Basestation.objects.all()
    serializer_class = BasestationSerializers
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneUserAuthenticated,)
    renderer_classes = (JSONRenderer,)
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend,)
    search_fields = ('name',)
    filter_fields = ('name',)


class BasestationDetails(generics.mixins.RetrieveModelMixin,
                         generics.mixins.UpdateModelMixin,
                         generics.mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    queryset = Basestation.objects.all()
    serializer_class = BasestationSerializers
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneUserAuthenticated,)
    renderer_classes = (JSONRenderer,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        list_broadcast = Broadcast.objects.filter(base_station=instance)
        if len(list_broadcast) > 0:
            msg = _('You cannot delete area if area have one or many base broadcast.')
            return JSONResponse({'status': 'error', 'error': msg},
                                status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return JSONResponse({'status': 'success'}, status=status.HTTP_204_NO_CONTENT)

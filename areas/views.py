# Create your views here.
from rest_framework import generics, filters, status
from rest_framework.renderers import JSONRenderer

from areas.models import Area
from areas.serializers import AreaSerializers
from basestations.models import Basestation
from broadcasting_manager.views import JSONResponse
from one_auth.authentication import OneTokenAuthentication
from one_users.permissions import IsOneUserAuthenticated


class AreaListView(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializers
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneUserAuthenticated,)
    renderer_classes = (JSONRenderer,)
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend,)
    search_fields = ('name',)
    filter_fields = ('name',)


class AreaDetails(generics.mixins.RetrieveModelMixin,
                  generics.mixins.UpdateModelMixin,
                  generics.mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializers
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneUserAuthenticated,)
    renderer_classes = (JSONRenderer,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        list_basestation = Basestation.objects.filter(area=instance)
        if len(list_basestation) > 0:
            msg = _('You cannot delete area if area have one or many base station.')
            return JSONResponse({'status': 'error', 'error': msg},
                                status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return JSONResponse({'status': 'success'}, status=status.HTTP_204_NO_CONTENT)

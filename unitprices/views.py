# Create your views here.
import datetime
import time

from rest_framework import generics, status
from rest_framework.renderers import JSONRenderer

from broadcasting_manager.views import JSONResponse
from one_auth.authentication import OneTokenAuthentication
from one_users.permissions import IsOneUserAuthenticated
from unitprices.models import Unitprice
from unitprices.serializers import UnitpriceSerializers


class UnitpriceListView(generics.ListCreateAPIView):
    queryset = Unitprice.objects.filter(is_delete=0)
    serializer_class = UnitpriceSerializers
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneUserAuthenticated,)
    renderer_classes = (JSONRenderer,)


class UnitpriceDetails(generics.mixins.RetrieveModelMixin,
                       generics.mixins.UpdateModelMixin,
                       generics.mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    queryset = Unitprice.objects.filter(is_delete=0)
    serializer_class = UnitpriceSerializers
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneUserAuthenticated,)
    renderer_classes = (JSONRenderer,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_delete = int(time.mktime(datetime.datetime.now().timetuple()))
        instance.save()
        return JSONResponse({'status': 'success'}, status=status.HTTP_204_NO_CONTENT)

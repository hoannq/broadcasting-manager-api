# Create your views here.
from rest_framework import generics, filters
from rest_framework.renderers import JSONRenderer

from contracts.models import Contract
from contracts.serializers import ContractSerializers
from one_auth.authentication import OneTokenAuthentication
from one_users.permissions import IsOneUserAuthenticated


class ContractListView(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializers
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneUserAuthenticated,)
    renderer_classes = (JSONRenderer,)
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend,)
    search_fields = ('broadcast',)
    filter_fields = ('broadcast',)


class ContractDetails(generics.mixins.RetrieveModelMixin,
                      generics.mixins.UpdateModelMixin,
                      generics.mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializers
    authentication_classes = (OneTokenAuthentication,)
    permission_classes = (IsOneUserAuthenticated,)
    renderer_classes = (JSONRenderer,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
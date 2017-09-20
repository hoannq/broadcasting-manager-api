from rest_framework import serializers

from machinelocations.models import Machinelocation


class MachinelocationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Machinelocation
        fields = ('id', 'name', 'owner',)
        # read_only_fields = ('unit')

from rest_framework import serializers

from basestations.models import Basestation


class BasestationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Basestation
        fields = '__all__'

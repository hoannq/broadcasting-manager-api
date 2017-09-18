from rest_framework import serializers

from broadcasts.models import Broadcast


class BroadcastSerializers(serializers.ModelSerializer):
    class Meta:
        model = Broadcast
        fields = '__all__'
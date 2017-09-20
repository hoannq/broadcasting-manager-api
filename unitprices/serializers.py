from rest_framework import serializers

from unitprices.models import Unitprice


class UnitpriceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Unitprice
        fields = ('id', 'broadcasting_hours', 'renew', 'power_type', 'price', 'machine_location',)

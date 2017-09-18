from rest_framework import serializers

from unitprices.models import Unitprice


class UnitpriceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Unitprice
        fields = '__all__'

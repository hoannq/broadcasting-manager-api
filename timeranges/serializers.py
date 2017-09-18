from rest_framework import serializers

from timeranges.models import Timerange


class TimerangeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Timerange
        fields = '__all__'

from django.db import models
from broadcastingstatus.models import Broadcastingstatus

# Create your models here.
TYPES = (
    (1, 'Khung giờ phát sóng'),
    (2, 'mất sóng do sự cố máy phát'),
    (3, 'mất sóng máy phát do nguyên nhân khác'),
    (4, 'mất sóng tín hiệu'),
)

class Timerange(models.Model):
    type = models.SmallIntegerField(choices=TYPES, default=TYPES[0][0])
    start_time = models.TimeField(blank=False, null=False)
    end_time = models.TimeField(blank=False, null=False)

    broadcasting_status = models.ForeignKey(Broadcastingstatus, on_delete=models.CASCADE)
from django.db import models
from basestations.models import Basestation

# Create your models here.
BROADCASTING_HOURS = ( ('19', '19'), ('24', '24') )
BROADCASTING_TYPES = ( ('Vệ tinh', 'Vệ tinh'), ('Số', 'Số'), ('Tương tự', 'Tương tự') )
TIME_SEGMENT = ((1, 1), (2, 2), (3, 3))

class Broadcast(models.Model):
    name = models.CharField(max_length=10, blank=False, null=False)
    contract_start_date = models.DateField(blank=False, null=False)
    contract_end_date = models.DateField(blank=False, null=False)
    broadcasting_hours = models.CharField(max_length=2, choices=BROADCASTING_HOURS, default=BROADCASTING_HOURS[1][0])
    frequency_channel = models.CharField(max_length=2, blank=True, null=True)
    power = models.CharField(max_length=6, blank=True, null=True)
    broadcasting_type = models.CharField(max_length=15, choices=BROADCASTING_TYPES, default=BROADCASTING_TYPES[2][0])
    time_segment = models.SmallIntegerField(choices=TIME_SEGMENT, default=1)
    machine_brand = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_by_contract = models.BooleanField(default=True, blank=False, null=False)
    is_by_region = models.BooleanField(default=False, blank=False, null=False)

    base_station = models.ForeignKey(Basestation, on_delete=models.CASCADE)

    class Meta:
        db_table = "broadcasts"

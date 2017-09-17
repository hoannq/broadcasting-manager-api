from django.db import models
from machinelocations.models import Machinelocation

# Create your models here.
BROADCASTING_HOURS = (
    (0, '19'), (1, '24')
)

POWER_TYPES = ((10, '10'), (5, '5'), (2, '2'))

class Unitprice(models.Model):
    broadcasting_hours = models.CharField(choices=BROADCASTING_HOURS, default=BROADCASTING_HOURS[1][1])
    renew = models.BooleanField(default=False, null=False)
    power_type = models.CharField(choices=POWER_TYPES, default=POWER_TYPES[1][1])
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=False, null=False)

    machine_location = models.OneToOneField(Machinelocation, blank=True, null=True)
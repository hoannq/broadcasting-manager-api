from django.db import models
from machinelocations.models import Machinelocation

# Create your models here.
BROADCASTING_HOURS = (
    ('19', '19'), ('24', '24')
)
POWER_TYPES = (('10', '10'), ('5', '5'), ('2', '2'))
RENEW = ( (1, 'Thứ nhất'), (0, 'Thứ hai') )

class Unitprice(models.Model):
    broadcasting_hours = models.CharField(max_length=2, choices=BROADCASTING_HOURS, default=BROADCASTING_HOURS[1][1])
    renew = models.SmallIntegerField(choices=RENEW, default=0, blank=False, null=False)
    power_type = models.CharField(max_length=2, choices=POWER_TYPES, default=POWER_TYPES[1][0])
    price = models.DecimalField(max_digits=10, decimal_places=0, blank=False, null=False)

    machine_location = models.ForeignKey(Machinelocation, blank=True, null=True)

    class Meta:
        db_table = "unit_prices"
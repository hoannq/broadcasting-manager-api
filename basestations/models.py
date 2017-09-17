from django.db import models
from televisions.models import Television
from areas.models import Area

# Create your models here.
MANAGE_TYPE = (
    ('Hợp đồng', 'Hợp đồng'),
    ('Trực tiếp', 'Trực tiếp')
)

class Basestation(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    alias_name = models.CharField(max_length=50, blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    location = models.CharField(max_length=100, blank=False, null=False)
    manage_type = models.CharField(max_length=10, choices=MANAGE_TYPE, default=0)
    description = models.TextField(blank=True, null=True)

    television = models.ForeignKey(Television, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, null=True, blank=True)

    class Meta:
        db_table = "base_stations"
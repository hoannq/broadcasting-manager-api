from django.db import models
from broadcasts.models import Broadcast

# Create your models here.
class Broadcastingstatus(models.Model):
    date = models.DateField(blank=False, null=False)
    power_T = models.CharField(max_length=10, blank=True, null=True)
    power_PX = models.CharField(max_length=10, blank=True, null=True)
    reporter = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    broadcast = models.ForeignKey(Broadcast, on_delete=models.CASCADE)
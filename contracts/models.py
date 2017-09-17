from django.db import models
from unitprices.models import Unitprice
from broadcasts.models import Broadcast

# Create your models here.
CONTRACT_TYPES = (
    (0, 'Khai thác'), (1, 'Tiếp phát')
)

TAX = ( (5, 5.00), (10, 10.00) )

class Contract(models.Model):
    contract_number = models.CharField(blank=False, null=False)
    sign_date = models.DateField(blank=False, null=False)
    contract_type = models.CharField(choices=CONTRACT_TYPES, default=CONTRACT_TYPES[0][1])
    tax = models.DecimalField(choices=TAX, default=TAX[1][1], max_digits=5, decimal_places=2)
    cancel_date = models.DateField(blank=True, null=True)

    broadcast = models.OneToOneField(Broadcast, on_delete=models.CASCADE)
    unit_price = models.ForeignKey(Unitprice, on_delete=models.CASCADE)
from django.db import models
from unitprices.models import Unitprice
from broadcasts.models import Broadcast

# Create your models here.
CONTRACT_TYPES = ( ('Khai thác', 'Khai thác'), ('Tiếp phát', 'Tiếp phát') )
TAX = ( (5.00, 5.00), (10.00, 10.00) )

class Contract(models.Model):
    contract_number = models.CharField(max_length=20, blank=False, null=False)
    sign_date = models.DateField(blank=False, null=False)
    contract_type = models.CharField(max_length=10, choices=CONTRACT_TYPES, default=CONTRACT_TYPES[0][0])
    tax = models.DecimalField(choices=TAX, default=TAX[1][0], max_digits=5, decimal_places=2)
    cancel_date = models.DateField(blank=True, null=True)

    broadcast = models.OneToOneField(Broadcast, on_delete=models.CASCADE)
    unit_price = models.ForeignKey(Unitprice, on_delete=models.CASCADE)
from django.db import models

# Create your models here.
class Television(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    province = models.CharField(max_length=50, blank=False, null=False)
    representative = models.CharField(max_length=50, blank=False, null=False)
    position = models.CharField(max_length=20, blank=False, null=False)
    address = models.TextField(blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    fax = models.CharField(max_length=15, blank=True, null=True)
    tax_code = models.CharField(max_length=15, blank=False, null=False)
    bank_account = models.CharField(max_length=15, blank=False, null=False)
    bank = models.CharField(max_length=100, blank=False, null=False)
    decision_number = models.CharField(max_length=20, blank=False, null=False)
    decision_date = models.DateField()
    description = models.TextField(blank=True, null=True)

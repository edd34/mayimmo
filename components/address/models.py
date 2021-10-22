from django.db import models


class Address(models.Model):
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=5)

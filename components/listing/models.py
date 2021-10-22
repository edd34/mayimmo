from django.db import models
from components.property.models import Property
from components.helpers.estate_type import EstateType

# Create your models here.


class Listing(models.Model):
    is_available = models.BooleanField()
    date_available = models.BooleanField()
    date_not_available = models.BooleanField()
    estate_type = models.TextField(choices=EstateType.choices)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    price = models.FloatField()
    active = models.BooleanField()

from django.db import models
from components.property.models import Property
from components.helpers.estate_type import EstateType

# Create your models here.


class Listing(models.Model):
    is_available = models.BooleanField()
    available_since = models.DateField(null=True)
    not_available_since = models.DateField(null=True)
    estate_type = models.TextField(choices=EstateType.choices)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    price = models.FloatField()
    active = models.BooleanField()

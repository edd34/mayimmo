from django.db import models
from components.property.models import Property
from components.helpers.estate_type import EstateType


class Listing(models.Model):
    is_available = models.BooleanField()
    available_since = models.DateField(null=True)
    not_available_since = models.DateField(null=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

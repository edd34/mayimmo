from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from components.address.models import Address
from components.helpers.property_type import PropertyType
from components.helpers.estate_type import EstateType


class Property(models.Model):
    area = models.FloatField("surface", blank=False, null=False)
    address = models.ForeignKey(to=Address, on_delete=CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    property_type = models.TextField(
        "type de propriété", choices=PropertyType.choices)
    estate_type = models.TextField(
        "type de transaction", choices=EstateType.choices)

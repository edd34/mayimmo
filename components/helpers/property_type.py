from django.db import models


class PropertyType(models.TextChoices):
    house = 'house'
    apartment = 'apartment'
    parking = 'parking'
    box = 'box'
    commercial_premise = 'commercial premise'
    shop = 'shop'

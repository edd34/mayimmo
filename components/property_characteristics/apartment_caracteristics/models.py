from django.db import models
from common_caracteristics.models import CommonCharacteristics, KitchenCharacteristics, OtherParts


class ApartmentCharacteristics(CommonCharacteristics, KitchenCharacteristics, OtherParts):
    furnished = models.BooleanField("meublé", default=False)
    garden = models.BooleanField("jardin", default=False)
    balcony = models.BooleanField("balcon", default=False)
    nice_view = models.BooleanField("belle vue", default=False)
    pool = models.BooleanField("piscine", default=False)
    terrace = models.BooleanField("terrasse", default=False)
    cupboard = models.BooleanField("placard", default=False)

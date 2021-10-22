from django.db import models
from components.helpers.orientation import Orientation


class CommonCharacteristics(models.Model):
    elevator = models.BooleanField("ascenseur", default=False)
    guardian = models.BooleanField("guardien", default=False)
    ground_floor = models.BooleanField("rez-de-chaussée", default=False)
    last_stage = models.BooleanField("dernier étage", default=False)
    security_device = models.BooleanField(
        "dispositif de sécurité", default=False)
    alarm = models.BooleanField(
        "alarme", default=False)
    handicap_access = models.BooleanField("accès handicapé", default=False)
    orientation = models.Choices("orientation", Orientation)
    open_parking = models.BooleanField("parking ouvert", default=False)
    box = models.BooleanField("box", default=False)

    class Meta:
        abstract = True


class KitchenCharacteristics(models.Model):
    separate_kitchen = models.BooleanField(
        "cuisine séparée", default=False)
    american_kitchen = models.BooleanField("cuisine américaine", default=False)
    kitchenette = models.BooleanField("kitchenette", default=False)
    equipped_kitchen = models.BooleanField("cuisine équipée", default=False)

    class Meta:
        abstract = True


class OtherParts(models.Model):
    separate_toilet = models.BooleanField("cuisine équipée", default=False)
    separate_entrance = models.BooleanField("entrée séparée", default=False)
    bathroom = models.BooleanField("salle de bain", default=False)
    shower_room = models.BooleanField("salle de douche", default=False)
    stay = models.BooleanField("séjour", default=False)
    dining_room = models.BooleanField("salle à manger", default=False)

    class Meta:
        abstract = True

from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from components.address.models import Address
from components.helpers.property_type import PropertyType
from components.helpers.estate_type import EstateType
from components.helpers.orientation import Orientation


class Property(models.Model):
    area = models.FloatField("surface", null=False)
    price = models.FloatField(null=True)
    address = models.ForeignKey(to=Address, on_delete=CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=1500, null=True)
    property_type = models.TextField(
        "type de propriété", choices=PropertyType.choices)
    estate_type = models.TextField(
        "type de transaction", choices=EstateType.choices)

    # main characteristics
    elevator = models.BooleanField("ascenseur", null=True)
    guardian = models.BooleanField("guardien", null=True)
    ground_floor = models.BooleanField("rez-de-chaussée", null=True)
    last_stage = models.BooleanField("dernier étage", null=True)
    security_device = models.BooleanField(
        "dispositif de sécurité", null=True)
    alarm = models.BooleanField(
        "alarme", null=True)
    handicap_access = models.BooleanField("accès handicapé", null=True)
    orientation = models.TextField(
        "orientation", choices=Orientation.choices, null=True)
    open_parking = models.BooleanField("parking ouvert", null=True)
    box = models.BooleanField("box", null=True)

    # kitchen
    separate_kitchen = models.BooleanField(
        "cuisine séparée", null=True)
    american_kitchen = models.BooleanField("cuisine américaine", null=True)
    kitchenette = models.BooleanField("kitchenette", null=True)
    equipped_kitchen = models.BooleanField("cuisine équipée", null=True)
    separate_toilet = models.BooleanField("cuisine équipée", null=True)

    # other pars
    separate_entrance = models.BooleanField("entrée séparée", null=True)
    bathroom = models.BooleanField("salle de bain", null=True)
    shower_room = models.BooleanField("salle de douche", null=True)
    stay = models.BooleanField("séjour", null=True)
    dining_room = models.BooleanField("salle à manger", null=True)

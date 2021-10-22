from django.db import models


class Orientation(models.TextChoices):
    north = 'N', "North"
    south = 'S', "South"
    east = 'E', "East"
    west = 'W', "West"

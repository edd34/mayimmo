from django.db import models


class EstateType(models.TextChoices):
    sale = 's', 'SALE'
    rental = 'r', 'RENTAL'

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model
from components.address.models import Address
from components.listing.models import Listing
from components.property.models import Property
from utils.management.commands.generate_fake_data import create_rows_faker_address, create_rows_faker_property, create_rows_faker_user
from django.db import transaction, IntegrityError
import pandas as pd
import numpy as np
from tqdm import tqdm
User = get_user_model()


class Command(BaseCommand):
    help = 'import database'

    def handle(self, *args, **kwargs):
        df_address = create_rows_faker_address(
            50)[["address_1", "city", "zip_code", "longitude", "latitude"]]
        df_user = create_rows_faker_user(50)
        df_property = create_rows_faker_property(50)
        df_address_dict = df_address.to_dict('records')
        df_user_dict = df_user.to_dict('records')
        df_property_dict = df_property.to_dict('records')

        def create_record(index):
            try:
                with transaction.atomic():
                    user = User.objects.create_user(
                        email=df_user_dict[index]["email"],
                        firstname=df_user_dict[index]["firstname"],
                        lastname=df_user_dict[index]["lastname"],
                        phone=df_user_dict[index]["phone"],
                        username=df_user_dict[index]["username"],
                        password=None
                    )
                    user.is_superuser = False
                    user.is_staff = False
                    address = Address.objects.create(**df_address_dict[index])
                    df_property_dict[index]["owner"] = user
                    df_property_dict[index]["address"] = address
                    property = Property.objects.create(
                        **df_property_dict[index])
            except Exception:
                print("Error", index)

        print("creating records in db")
        for i in tqdm(range(len(df_property_dict))):
            create_record(i)

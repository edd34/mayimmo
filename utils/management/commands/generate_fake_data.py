import geopandas as gpd
import pandas as pd
from faker import Faker
import random
import os
from tqdm import tqdm

fake = Faker(locale='fr_FR')

nb_data = 50


def create_rows_faker_address(num=nb_data):
    print("* Reading ADRESSE shapefile")
    df_address = gpd.read_file(
        './utils/management/commands/geodata/ADRESSE.shx', encoding='utf-8')
    print("* Reading COMMUNE shapefile")
    df_commune = gpd.read_file(
        './utils/management/commands/geodata/COMMUNE.shx', encoding='utf-8')
    res = gpd.sjoin(df_address, df_commune,  predicate='within')

    # apply filters
    res = res[
        (res["NOM_1"] != res["NOM"])
    ]

    print("generating addresses")
    result = []
    for i in tqdm(range(len(df_commune))):
        tmp_res = df_commune["NOM"].iloc[i]
        tmp_result = res[(res["NOM"] == tmp_res)].sample(num)[["NUMERO", "NOM_1", "CODE_POST_left",
                                                               "NOM", "geometry", "COTE", "METHODE"]]
        tmp_result["address_1"] = tmp_result["NUMERO"].astype(
            'str')+' ' + tmp_result["NOM_1"]
        tmp_result.rename(
            columns={'CODE_POST_left': 'zip_code', 'NOM': 'city'}, inplace=True)
        result.append(tmp_result)

    # pprint(result)
    rdf = gpd.GeoDataFrame(pd.concat(result, ignore_index=True))
    rdf["longitude"] = rdf["geometry"].x
    rdf["latitude"] = rdf["geometry"].y
    rdf.drop(['geometry', "COTE", "METHODE"], axis=1,
             inplace=True)
    return rdf


def create_rows_faker_user(num=nb_data):
    print("generating users")
    output = [{"firstname": fake.first_name(),
               "lastname": fake.last_name(),
               "email": fake.ascii_email(),
               "phone": fake.phone_number(),
               "username": fake.user_name()} for _ in tqdm(range(17*num))]
    return pd.DataFrame(output)


def create_rows_faker_property(num=nb_data):
    print("generating property")
    result = []
    for _ in tqdm(range(17*num)):
        area = fake.pyfloat(min_value=15, max_value=70)
        price = fake.pyfloat(min_value=7, max_value=15)
        output = {
            "area": area,
            "price": price*area,
            "title": fake.sentence(nb_words=10),
            "description": fake.paragraph(nb_sentences=10),
            "property_type": "apartment",
            "estate_type": "r",
            "elevator": fake.pybool(),
            "guardian": fake.pybool(),
            "ground_floor": fake.pybool(),
            "last_stage": fake.pybool(),
            "security_device": fake.pybool(),
            "alarm": fake.pybool(),
            "handicap_access": fake.pybool(),
            "orientation": random.choice("NSEW"),
            "open_parking": fake.pybool(),
            "box": fake.pybool(),
            "separate_kitchen": fake.pybool(),
            "american_kitchen": fake.pybool(),
            "kitchenette": fake.pybool(),
            "equipped_kitchen": fake.pybool(),
            "separate_toilet": fake.pybool(),
            "separate_entrance": fake.pybool(),
            "bathroom": fake.pybool(),
            "shower_room": fake.pybool(),
            "stay": fake.pybool(),
            "dining_room": fake.pybool()
        }
        result.append(output)
    return pd.DataFrame(result)


def export_to_csv(dataframe, file_name=r'export.csv'):
    dataframe.to_csv(file_name)

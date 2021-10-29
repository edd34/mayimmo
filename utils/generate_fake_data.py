import geopandas as gpd
import pandas as pd
from faker import Faker
import random

fake = Faker(locale='fr_FR')

nb_data = 10


def create_rows_faker_address(num=nb_data):
    df_address = gpd.read_file('geodata/ADRESSE.shx', encoding='utf-8')
    df_commune = gpd.read_file('geodata/COMMUNE.shx', encoding='utf-8')
    res = gpd.sjoin(df_address, df_commune,  predicate='within')

    # apply filters
    res = res[
        (res["NOM_1"] != res["NOM"])
    ]

    result = []
    for i in range(len(df_commune)):
        tmp_res = df_commune["NOM"].iloc[i]
        tmp_result = res[(res["NOM"] == tmp_res)].sample(num)[["NUMERO", "NOM_1", "CODE_POST_left",
                                                               "NOM", "geometry", "COTE", "METHODE"]]
        result.append(tmp_result)

    # pprint(result)
    rdf = gpd.GeoDataFrame(pd.concat(result, ignore_index=True))
    rdf["lon"] = rdf["geometry"].x
    rdf["lat"] = rdf["geometry"].y
    rdf.drop(['geometry', "COTE", "METHODE"], axis=1,
             inplace=True)
    return rdf


def create_rows_faker_user(num=nb_data):
    output = [{"firstname": fake.first_name(),
               "lastname": fake.last_name(),
               "email": fake.ascii_email(),
               "phone": fake.phone_number(),
               "username": fake.user_name()} for _ in range(17*num)]
    return output


def create_rows_faker_property(num=nb_data):
    result = []
    for _ in range(17*num):
        area = fake.pyfloat(min_value=15, max_value=70)
        price = fake.pyfloat(min_value=7, max_value=15)
        output = {
            "area": area,
            "price": price,
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
    return result


def export_to_csv(dataframe, file_name=r'export.csv'):
    dataframe.to_csv(file_name)


if __name__ == '__main__':
    rdf = create_rows_faker_address(nb_data)
    df_user_faker = pd.DataFrame(create_rows_faker_user(nb_data))
    df_property_faker = pd.DataFrame(create_rows_faker_property(nb_data))
    final_df = pd.concat([rdf, df_user_faker, df_property_faker], axis=1)
    print(final_df)
    export_to_csv(final_df)

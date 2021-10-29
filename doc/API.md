# API MayImmo

In this file you will find documentation about the Kamusy API.
The base API URL is http://141.94.223.19:8009

## 1. Property component

### a. Get all properties

-     GET: /property/

Description : return a JSON containing all properties in the database (**`deprecated`** because it uses a lot a network resources)
Example : [http://141.94.223.19:8009/property/](http://141.94.223.19:8009/property/)

Examples :

- http://141.94.223.19:8009/paginated-property/
- http://141.94.223.19:8009/paginated-property/?page=2
- http://141.94.223.19:8009/paginated-property/?page_size=5
- http://141.94.223.19:8009/paginated-property/?page=2&page_size=5

#### Example result

```json
[
  {
    "id": 1,
    "address": {
      "id": 1,
      "address_1": "20 R DU QUARTIER LA ROSE",
      "address_2": null,
      "city": "Kani-Kéli",
      "zip_code": "97625",
      "longitude": 511860.6,
      "latitude": 8567899.1
    },
    "owner": {
      "id": 1,
      "email": "legroslaurence@hotmail.fr",
      "firstname": "Adrien",
      "lastname": "Barbier",
      "username": "denis44",
      "phone": "+33 (0)4 67 70 42 05"
    },
    "area": 34.792,
    "price": 386.88419366648003,
    "title": "Appartenir où nouveau mal beau bois erreur écarter trois patron rocher.",
    "description": "Coucher extraordinaire abattre froid demain colon appuyer. Moyen compter préparer aventure perdre attention agir. Espace sentir chacun difficile élever. Regarder risquer venir désespoir. Plaine gauche professeur rocher. Entretenir faim troisième armée parvenir aspect. Grand monsieur possible fou travail entre épaule corps. Souvenir lisser cri lisser compte ouvert sentiment. Comprendre douleur transformer que doigt. Rencontre préparer livre côté peau.",
    "property_type": "apartment",
    "estate_type": "r",
    "elevator": true,
    "guardian": true,
    "ground_floor": false,
    "last_stage": false,
    "security_device": false,
    "alarm": false,
    "handicap_access": false,
    "orientation": "S",
    "open_parking": true,
    "box": false,
    "separate_kitchen": false,
    "american_kitchen": false,
    "kitchenette": true,
    "equipped_kitchen": true,
    "separate_toilet": true,
    "separate_entrance": false,
    "bathroom": true,
    "shower_room": true,
    "stay": true,
    "dining_room": false
  },
  { "id": 2,
     ...
   }
]
```

### b. Get paginated properties

-     GET: /paginated-property/

Description : return a JSON containing all properties in the database
Example : [http://141.94.223.19:8009/paginated-property/](http://141.94.223.19:8009/paginated-property/)

URL Params :

- `page=2` :
- `page_size=5`

Examples :

- http://141.94.223.19:8009/paginated-property/
- http://141.94.223.19:8009/paginated-property/?page=2
- http://141.94.223.19:8009/paginated-property/?page_size=5
- http://141.94.223.19:8009/paginated-property/?page=2&page_size=5

#### Example result

```json
{
  "count": 850,
  "next": "http://141.94.223.19:8009/paginated-property/?page=2&page_size=5",
  "previous": null,
  "results": [
    {
      "id": 1,
      "address": {
        "id": 1,
        "address_1": "20 R DU QUARTIER LA ROSE",
        "address_2": null,
        "city": "Kani-Kéli",
        "zip_code": "97625",
        "longitude": 511860.6,
        "latitude": 8567899.1
      },
      "owner": {
        "id": 1,
        "email": "legroslaurence@hotmail.fr",
        "firstname": "Adrien",
        "lastname": "Barbier",
        "username": "denis44",
        "phone": "+33 (0)4 67 70 42 05"
      },
      "area": 34.792,
      "price": 386.88419366648003,
      "title": "Appartenir où nouveau mal beau bois erreur écarter trois patron rocher.",
      "description": "Coucher extraordinaire abattre froid demain colon appuyer. Moyen compter préparer aventure perdre attention agir. Espace sentir chacun difficile élever. Regarder risquer venir désespoir. Plaine gauche professeur rocher. Entretenir faim troisième armée parvenir aspect. Grand monsieur possible fou travail entre épaule corps. Souvenir lisser cri lisser compte ouvert sentiment. Comprendre douleur transformer que doigt. Rencontre préparer livre côté peau.",
      "property_type": "apartment",
      "estate_type": "r",
      "elevator": true,
      "guardian": true,
      "ground_floor": false,
      "last_stage": false,
      "security_device": false,
      "alarm": false,
      "handicap_access": false,
      "orientation": "S",
      "open_parking": true,
      "box": false,
      "separate_kitchen": false,
      "american_kitchen": false,
      "kitchenette": true,
      "equipped_kitchen": true,
      "separate_toilet": true,
      "separate_entrance": false,
      "bathroom": true,
      "shower_room": true,
      "stay": true,
      "dining_room": false
    },
    {...}
  ]
}
```

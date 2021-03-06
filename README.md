# MayImmo

This is the backend of a Real Estate MLS for Mayotte Island. The project is done using :

- Python
- Django DRF
- Geopandas
- Pandas
- Faker

## Configure the virtual environment

### Create a new environment virtualenv

Create a virutal environment using [virtualenv](https://docs.python.org/fr/3/library/venv.html).

```bash
python3 -m venv venv
```

### Entering the environment

```bash
source venv/bin/activate
```

## Installation of package listed in requirement.txt

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
pip3 install -r requirements.txt
```

## Steps when running the program for the first time.

In order to run the backend program, you should follow the steps described below. All commands are run from the root folder.

### Refreshing migrations

```bash
python manage.py makemigrations
```

### Applying migrations

```bash
python manage.py migrate
```

### Import a sample database from CSV

```bash
python manage.py importdb
```

## Run the program

After the database is populated and correctly setup, you can run the backend server by executing the following command :

```bash
python manage.py runserver
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

### API doc

The documentation of the public API is available under doc folder : [API.md](doc/API.md)

## License

[MIT](https://choosealicense.com/licenses/mit/)

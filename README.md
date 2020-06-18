# Shoe Store API

Use of the Django REST framework and a fresh Django server to create an API for a shoe store with this repository: [https://github.com/luisfff29/drf_shoestore_api](https://github.com/luisfff29/drf_shoestore_api/]) and display it with a React app through this repository:
[https://github.com/luisfff29/drf_shoestore_frontend](https://github.com/luisfff29/drf_shoestore_frontend/])

## Installation

Use the package manager [poetry](https://python-poetry.org/) to install the Django API version.

```bash
poetry install
```

Then, start a virtual environment with the following command:

```bash
poetry shell
```

Before move on to run the server don't forget to populate a couple of tables with:

```bash
python manage.py bootstrap_data
```

Finally, you are ready to run the server with

```bash
python manage.py runserver
```

and check out the Shoe Store API built with Django in this [link](http://localhost:8000/api).

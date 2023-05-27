# django-quickstart

## Repo of a basic django poll app with admin features.

### Prerequisites 

- Python 3.10
- pipenv

### Set up

0. Run this command to install dependencies: `pipenv install`
0. Enter Virtual Environment: `pipenv shell`
0. Run database migrations: `python manage.py migrate`
0. Use: `python manage.py createsuperuser` to Create Admin. Fill in Name and Password.

### Running Server

0. Enter Virtual Environment: `pipenv shell`
0. Use: `python manage.py runserver` to boot up server 

## Features

1. Login in to ..../admin/ with your Superuser info
2. Can add, name and delete polls questions then save changes.
3. Test new poll by going to ..../polls/ after saved in admin panel. If if poll shows up the admin panel is working.

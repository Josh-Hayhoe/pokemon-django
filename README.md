# Pokémon Django

## Requirements

This application requires Python 3.

## Good to know

The application uses the [Django](https://www.djangoproject.com) web framework to take care of the boilerplate code and 
provide project structure.

This project is using `requirements.txt` at its most basic level. e.g. it's not configured to deal with new package releases, 
different environments etc.

You will need to have a MySQL server and database running on localhost set up by some means. 
The project is already set up to use mySQL, connection settings can be edited in the settings file `DJANGO_SETTINGS_MODULE` 
referenced in `manage.py`.

## Get started

1. Clone this repository to your local machine
```commandline
git clone repo-url-tbc
```
2. Navigate to the project folder
```commandline
cd pokemon-django
```
3. Create a virtual environment
```commandline
python -m venv venv
```
4. Activate the virtual environment you just created
```commandline
.\venv\Scripts\activate
```
5. Install packages
```commandline
python -m pip install -r requirements.txt
```
6. Add your database connection settings
7. Run migrations to create database tables
```commandline
python manage.py makemigrations
python manage.py migrate
```
8. start the development server
```commandline
python manage.py runserver
```

## Working tips

Pinning package requirements:
```commandline
python -m pip freeze > requirements.txt
```

Deactivate the virtual environment:
```commandline
deactivate
```

Before activating virtual environment:
Set-ExecutionPolicy Unrestricted -Scope Process



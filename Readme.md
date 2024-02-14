# Django Sample App

To get started you need to have pip installed

Create a venv in the current folder (Python 3.10)

```console
python3.10 -m venv env
```

Activate the virtual environment

```console
source env/bin/activate  
```

Install dependencies

```console
pip install -r requirements.txt 
```
Run migrations in local sqlite db

```console
python manage.py migrate
```
Create super user

```console
python manage.py createsuperuser --username admin --email admin@example.com
```
Run the server
```console
python manage.py runserver
```

Navigate to login page open http://localhost:8000/api/auth/login and enter the selected email and password of the super user

Navigate to the API root http://localhost:8000/api/

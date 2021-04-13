# Contact Form
Django Project web application

[See a demo of the website here](https://fc-contactform.herokuapp.com/contactformapp/)

This is just a web page with a contact form.  I created this project to get familiar with forms and learn how to configure the e-mail settings.

When the form is submitted, data is saved to database and emailed to the list of admins specified in `ADMINS` in settings.py.

## Instructions
Clone this project
```
https://github.com/timamero/django-recipe-please.git
```

Install Dependencies
```
pip install -r requirements.txt
```

Update settings.py Variables
```
SECRET_KEY 
EMAIL_HOST
EMAIL_PORT
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD
ADMINS
```

Run Database Migrations
```
py manage.py makemigrations
py manage.py migrate
```

Create Superuser
```
py manage.py createsuperuser
```
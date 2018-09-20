# Django Starter Template (Python)

django-rest boilerplate for 4Geeks Academy students (ready for deployment on heroku if needed)

## Features

- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Latest Python 3.6 runtime environment.

## How to Use

To use this project, follow these steps:

1. Make sure you have python 3.6 installed, if you are using Cloud 9 you can install it by typing:
```sh
$ pyenv install 3.6.6   (this step takes a while)
$ pyenv global 3.6.6
```
2. Install [Django](https://www.djangoproject.com/) and [pipenv](https://pipenv.readthedocs.io/en/latest/) (`$ sudo pip install django pipenv`)
3. Make sure your current folder is empty. `$ ls` (if you do `ls`, it should show nothing, no files)
4. Create a new project using the 4Geeks Academy django-rest-hello template:
```sh
$ django-admin startproject <your_project_name> . --template=https://github.com/4GeeksAcademy/django-rest-hello/archive/master.zip --name=Procfile
```

You can replace ``<your_project_name>`` with your desired project name.
5. Install any defaul packages (similar to `npm install` when using javascript) and get inside your recently created python envirnoment
```sh
$ pypenv install
$ pipenv shell
```

6. Run the migrations
```sh
$ python manage.py migrate
```

7. Start the python server
```sh
$ python manage.py runserver $IP:$PORT
```

## What next?

Your python API should be running smoothly.


## Deploy your project to Heroku

```sh
$ git init
$ git add -A
$ git commit -m "Initial commit"

$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
```

### Aditional Tutorials
- [Working with django /admin](quick_tutorials/ADMIN.md) to create superusers, add models to your admin, etc.
- [Using the shell](quick_tutorials/DATABASE_API.md) to CRUD models, etc.
- [Working with Migrations](quick_tutorials/MIGRATIONS.md) for everytime you change your model
- [Using MySQL](quick_tutorials/MYSQL.md) insalling and using MySQL in your application.
- [Using Mongo](quick_tutorials/MONGO.md) insalling and using mongo in your application.
- [Working with OAuth](quick_tutorials/OAUTH.md) implementing OAuth with the JWT Oauth Toolkit.

## Packages Being Used (Documentation)
- [Django CORS Headers](https://github.com/ottoyiu/django-cors-headers)
- [Django REST Framework](https://github.com/encode/django-rest-framework)

# API Starter Template (Python & Django REST)

A django-rest boilerplate for 4Geeks Academy students. It features ready-for-deployment on heroku instructions.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io#https://github.com/4GeeksAcademy/django-rest-hello.git)

## Features

- Ready to deploy to heroku in just 1 minute (for free).
- 100% compatible with gitpod.

### 1) Install any default packages (similar to `npm install` when using javascript) and get inside your recently created python envirnoment
```sh
$ pipenv install
```

### 2) Run migrations
1. `$ pipenv run migrate` Run database migration
2. `$ pipenv run start` Run the server

## What next?

Your python API should be running smoothly. You should [read the docs for tutorials](https://github.com/4GeeksAcademy/django-rest-hello/tree/master/docs).

You can go ahead and add/update the following files:
- api/models.py to include more tables/entities into your database.
- api/urls.py  to include more endpoints and match them with views
- views.py to specify wich methods will apply to each endpoint (GET, POST, PUT, DELETE)

### Aditional Tutorials
- [Working with django /admin](https://github.com/4GeeksAcademy/django-rest-hello/blob/master/docs/ADMIN.md) to create superusers, add models to your admin, etc.
- [Using the python shell](https://github.com/4GeeksAcademy/django-rest-hello/blob/master/docs/DATABASE_API.md) to CRUD models, etc.
- [Working with Migrations](https://github.com/4GeeksAcademy/django-rest-hello/blob/master/docs/MIGRATIONS.md) for everytime you change your model
- [Using MySQL](https://github.com/4GeeksAcademy/django-rest-hello/blob/master/docs/MYSQL.md) insalling and using MySQL in your application.
- [Using Mongo](https://github.com/4GeeksAcademy/django-rest-hello/blob/master/docs/MONGO.md) insalling and using mongo in your application.

## Packages Being Used (Documentation)
- [Django CORS Headers](https://github.com/ottoyiu/django-cors-headers)
- [Django REST Framework](https://github.com/encode/django-rest-framework)

## Deploy your project to Heroku
If you don't have your code connected to a github repository, please do it:
```
$ git init
$ git add -A
$ git commit -m "Initial commit"
```
Then, run these 3 steps to deploy to heroku:
```sh
$ heroku create
$ git push heroku master

$ heroku run python manage.py migrate
```

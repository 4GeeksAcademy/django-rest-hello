# API Starter Template (Python & Django REST)

django-rest boilerplate for 4Geeks Academy students (ready for deployment on heroku if needed)

## Features

- It uses the latest python.
- Ready to deploy to heroku in just 1 minute (for free).
- 100% compatible with Cloud 9

## How to Use :question:

To use this project, follow these steps:

1. Make sure you have python 3.6 installed, if you are using Cloud 9 you can install it by typing:
```sh
$ pyenv install 3.6.6   (this step takes a while)
$ pyenv global 3.6.6
```
2. Install [Django](https://www.djangoproject.com/) and [pipenv](https://pipenv.readthedocs.io/en/latest/) (`$ sudo pip install django pipenv`)

##### :warning: Only run these steps 3 & 4 if you are the one starting the project from scratch

3. Make sure your current folder is empty. `$ ls` (if you do `ls`, it should show nothing, no files)
4. Create a new project using the 4Geeks Academy django-rest-hello template:
```sh
$ django-admin startproject <your_project_name> . --template=https://github.com/4GeeksAcademy/django-rest-hello/archive/master.zip --name=Procfile
```
Note: You can replace ``<your_project_name>`` with your desired project name.

##### :warning: Everyone needs to run these 5,6,7 commands.

5. Install any default packages (similar to `npm install` when using javascript) and get inside your recently created python envirnoment
```sh
$ pipenv install
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

### Aditional Tutorials
- [Working with django /admin](https://github.com/4GeeksAcademy/django-rest-hello/blob/master/docs/ADMIN.md) to create superusers, add models to your admin, etc.
- [Using the python shell](https://github.com/4GeeksAcademy/django-rest-hello/blob/master/docs/DATABASE_API.md) to CRUD models, etc.
- [Working with Migrations](https://github.com/4GeeksAcademy/django-rest-hello/blob/master/docs/MIGRATIONS.md) for everytime you change your model
- [Using MySQL](https://github.com/4GeeksAcademy/django-rest-hello/blob/master/docs/MYSQL.md) insalling and using MySQL in your application.
- [Using Mongo](https://github.com/4GeeksAcademy/django-rest-hello/blob/master/docs/MONGO.md) insalling and using mongo in your application.

## Packages Being Used (Documentation)
- [Django CORS Headers](https://github.com/ottoyiu/django-cors-headers)
- [Django REST Framework](https://github.com/encode/django-rest-framework)

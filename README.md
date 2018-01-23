# Installation


1) Change your python version to 3

```sh
$ sudo mv /usr/bin/python /usr/bin/python2 
$ sudo ln -s /usr/bin/python3 /usr/bin/python
```

2) Download django

```sh
$ sudo pip install django
```

3) Start a django website

```sh
$ django-admin startproject <project-name>
& cd <project-name>
```
A django project is divided in one or more apps, that way you can re-use any app on other proyects.

4) Create your first app

```sh
$ python manage.py startapp <app1_name>
```

5) Run the migrations

```sh
$ python manage.py migrate
```

6) Add your website URL to the ALLOWED_HOSTS on settings.py

```python
ALLOWED_HOSTS = [
    'django-example-alesanchezr.c9users.io',
    ]
```


7) Run django on c9 ports by doing 

```sh
$ python manage.py runserver $IP:$PORT
```

## Aditional Tutorials
/blob/master/quick_tutorials/ADMIN.md
- [Create admin users](quick_tutorials/ADMIN.md) to create users, etc.
- [Typical workflow for any API method](quick_tutorials/CREATING_API_METHODS.md) to create users, etc.
- [Working with the database objects](quick_tutorials/DATABASE_API.md) to create users, etc.
- [Working with Migrations](quick_tutorials/MIGRATIONS.md) to create users, etc.
- [Using Mongo](quick_tutorials/MONGO.md) to create users, etc.

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
```
In django every page of the website is an "app", you should reak your website en very little parts, each part being an "app"

4) Create your first app

```sh
$ python manage.py startapp <app1_name>
```
5) Create a urls.py on your <app1_name> folder and add the following

```py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```

6) Update the <project-name>/urls.py to include the <app1_name> app

```python
#project URL Configuration

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^<app1_name>/', include('<app1_name>.urls')),
    url(r'^admin/', admin.site.urls),
]
```

7) Create the index view inside the <app1_name>/view.py file

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>employees!!!!</h1>')
```

8) Run the migrations

```sh
$ python manage.py migrate
```

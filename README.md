# Installation


1) Change your python version to 3

```sh
$ sudo mv /usr/bin/python /usr/bin/python2 
$ sudo ln -s /usr/bin/python3 /usr/bin/python
```

2) Start a django website

```sh
$ django-admin start-project fetes
```

In django every page of the website is an "app", you should reak your website en very little parts, each part being an "app"

3) Create your first app

```sh
$ python manage.py startapp employees
```
4) Create a urls.py on your employees folder and add the following

```py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```

5) Update the fetes/urls.py to include the employees app

```python
#fetes URL Configuration

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^employees/', include('employees.urls')),
    url(r'^admin/', admin.site.urls),
]
```

6) Create the  index views

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>employees!!!!</h1>')
```

7) Run the migrations

```sh
$ python manage.py migrate
```
# Coding your first app

1) Create a urls.py on your <app1_name> folder and add the following

```py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```

2) Update the <project-name>/urls.py to include the <app1_name> app

```python
#project URL Configuration

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^<app1_name>/', include('<app1_name>.urls')),
    url(r'^admin/', admin.site.urls),
]
```

3) Create the index view inside the <app1_name>/view.py file

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>employees!!!!</h1>')
```
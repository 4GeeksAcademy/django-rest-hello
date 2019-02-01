# API Starter Template (Python & Django REST)

A django-rest boilerplate for 4Geeks Academy students. It features ready-for-deployment on heroku instructions.

## Features

- It uses the latest python version (as of Oct 2018).
- Ready to deploy to heroku in just 1 minute (for free).
- 100% compatible with [c9.io](http://c9.io) .

## How to install this project :question:

Follow these steps:

1. Make sure you have python 3.6 installed, if you are using Cloud9 you can install it by typing:
```sh
$ pyenv install 3.6.6   (this step takes a while)

$ pyenv global 3.6.6
```

2. Install [Django](https://www.djangoproject.com/) and [pipenv](https://pipenv.readthedocs.io/en/latest/) 
```sh
$ sudo pip install django pipenv
```

##### :warning: Only run these steps 3 & 4 if you are starting the project from scratch

3. Make sure your current folder is empty. 
```sh
$ ls
```
It should show no files or folders.

4. Create a new project using the 4Geeks Academy django-rest-hello template:
```sh
$ django-admin startproject <project_name> . --template=https://github.com/4GeeksAcademy/django-rest-hello/archive/master.zip --name=Procfile
```
Note: You can replace ``<project_name>`` with your desired project name.

##### :warning: All team members need to run these 5,6,7 steps.

5. Install any default packages (similar to `npm install` when using javascript) and get inside your recently created python envirnoment
```sh
$ pipenv install

$ pipenv shell
```

6. Run migrations
```sh
$ python manage.py migrate
```

7. Start the python server
```sh
$ python manage.py runserver $IP:$PORT
```

## What next?

Your python API should be running smoothly.

## Installing [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/) (better documentation) for your API (Optional but recommended)
The API is up and running but it is very complicated to read and use, let's improve that. drf-yasg will use the Django-DRF implementation and generate a descriptive (and awesome) documentation. 

1. Install drf-yasg, make sure you are running the environment ( ```pipenv shell``` ):
  ```
  $ pipenv install drf-yasg
  ```
  Note: if you get "permission" errors, use ```sudo pipenv install drf-yasg``` instead.
  
2. In ```settings.py```:
  ```python
  INSTALLED_APPS = [
     ...
     'drf_yasg',
     ...
  ]
  ```
  
3. In ```urls.py```:
  ```python
  ...
  
  from django.contrib import admin
  from django.urls import path, include
  from django.conf.urls import url
  from rest_framework.documentation import include_docs_urls

  from drf_yasg.views import get_schema_view
  from drf_yasg import openapi

  schema_view = get_schema_view(
     openapi.Info(
        title="Contacts API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
     ),
     public=True,
  )

  urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/', include('api.urls')),
      path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
  ]
  ```
  
Now check your base url to see your endpoints' documentation.

To expand this information, you can use Comments and Decorators on each method inside ```views.py```. Here's an example code using the Contacts Boilerplate (already installed):

- The Comments after the ```class ContactsView(APIView):``` line are used as descriptions of each method for the entity's endpoint.

- The ```python @swagger_auto_schema( ... )```, is the information expected and the possible responses based on the methods' execution.

```python
...
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class ContactsView(APIView):
  """
  get:
  Return a list of all existing contacts

  post:
  Create a new contact
  """
  @swagger_auto_schema(
      responses={ 
          status.HTTP_200_OK : ContactSerializer(many=True),
          status.HTTP_404_NOT_FOUND : openapi.Response(description="No contact"),
      }
  )
  def get(self, request, contact_id=None):
      ...
      #this method will return
      # - 200_OK if contacts found
      # - 404_BAD_REQUEST if contact not found
      ...
      
      
  @swagger_auto_schema(
      request_body=ContactSerializer,
      responses={ 
          status.HTTP_200_OK : ContactSerializer,
          status.HTTP_400_BAD_REQUEST: openapi.Response(description="Missing information")
      }
  )
  def post(self, request):
      ...
      #this method will return 
      # - 200_OK if information in request is valid 
      # - 404_BAD_REQUEST otherwise.
      ...
   ...

```

Documentation with swag!





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

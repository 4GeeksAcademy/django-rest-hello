# Using MySQL with django

1) Install mysql in your computer
```
mysql-ctl install
```

2) Install the django mysql php package 
```
sudo pip install django mysqlclient
```

3) In your settings.py look for the DATABASE variable and replace the defaul object with the following:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

4) Run the migrations again

```
$ python manage.py migrate
```

## To install PHPMyAdmin

1) Change apache port to 8081 inside ports.conf
```
$ sudo vi /etc/apache2/ports.conf                                                                                           
```
2) Change apache port to 8081 inside 001-cloud9.conf
```
$ sudo vi /etc/apache2/sites-available/001-cloud9.conf
```
3) Restart apache
```
$ sudo service apache2 restart
```





```sh
$ python manage.py createsuperuser
```
Now you can login to the /admin

## To add more models to the admin, add the following to the employees/admin.py file
```python
admin.site.register(Employee)
```

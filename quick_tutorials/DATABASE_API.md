# django database API

To start first type:

```
$ python manage.py shell
```

That will start the python database API

Import the models you want to work with:
```
from employees.models import Employee, Department
```
Print all departments
```
Department.objects.all()
```
Create a department
```
dep = Department(name='My First Department')
```
Filter
```
Department.objects.filter(id=1)
Department.objects.filter(name__startswith='Ac')
Department.objects.get(id=1)
```

Get relation

dep.employee_set.all()

Set relation
dep = Department()
em2.department = dep

dep.employee_set.create() #emproyee parameters
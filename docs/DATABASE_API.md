# django database API

#### 1) Get into the python shell by typing:
```sh
$ python manage.py shell
```
Note: That will start the python database API

#### 2) Import the models you want to work with:
```py
from <your_application_name>.models import Department
```

#### 3) Use normal python to play with the models:

Print all departments (supposing you have a departmen Model)
```py
Department.objects.all()
```
Create a department (supposing you have a Department Model)
```py
dep = Department(name='My First Department')
```
Filtering departments (supposing you have a Department Model)
```py
# get an array of departments with the name starting with the word "Coordination"
departments = Department.objects.filter(name__startswith='Coordination')

# get one department with the id=1
department = Department.objects.get(id=1)
```

Get all employees from the department (many to many relation)
```py
dep = Department.objects.get(id=1)
dep.employee_set.all()
```
Add one employee to the deparment list of employees
```py
dep = Department.objects.get(id=1)
dep.employee_set.create(first_name='Juan') # you can specify all the employee information, not just the first_name
```

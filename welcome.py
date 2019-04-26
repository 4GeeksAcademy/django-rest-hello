"""
generate random keys for django
"""
import random

result = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])

print("""



             WELCOME GEEK! 🐍 + 💻 = 😀




Please copy the collowing key and paste it as the SECRET_KEY variable value on the example-project/settings.py:

\033[94m SECRET_KEY = \033[93m""" + result + """\033[0m

Afterwards you need to run the following commands to start coding:

- \033[94m$ pipenv shell\033[0m initiate the environtment
- \033[94m$ python manage.py migrate\033[0m run migrations (if pending)
- \033[94m$ python manage.py runserver $IP:$PORT\033[0m start django

""")

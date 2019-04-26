"""
generate random keys for django
"""
import random

result = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])

print("""
Please copy the collowing key and paste it as the SECRET_KEY variable value on the example-project/settings.py:

\033[94m SECRET_KEY = \033[93m""" + result + """\033[0m

""")

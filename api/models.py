"""
All your application modules and serializers are going to be declared inside this file
"""
from rest_framework import serializers
from django.db import models

"""
Define he Contact Entity into your applcation model
"""
class Contact(models.Model):
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    phone_number = models.CharField(max_length=15, default='')
    email = models.CharField(max_length=150, default='')

"""
The ContactSerializer is where you will specify what properties
from the ever Contact should be inscuded in the JSON response
"""
class ContactSerializer(serializers.ModelSerializer):


    class Meta:
        model = Contact
        # what fields to include?
        fields = ('first_name','last_name', 'phone_number', 'email')

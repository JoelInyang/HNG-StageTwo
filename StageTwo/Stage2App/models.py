from django.db import models
from django import forms
from django.core.exceptions import ValidationError 
from django.utils.translation import gettext_lazy as _

def validate_name_is_string(value):
    if not isinstance(value, str):
        raise ValidationError("Name should be a string.")
    try:
        int(value)  # Attempt to convert the string to an integer
        raise ValidationError("Name should not be a numeric value.")
    except ValueError:
        pass  # It's a string   

class Person(models.Model):
    name = models.CharField(max_length=255, validators=[validate_name_is_string])
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
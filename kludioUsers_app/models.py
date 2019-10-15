from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class users(models.Model):
    name =  models.CharField(max_length=200, default='')
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^(?:\+?88)?01[1-9]\d{8}$',
                                 message="Invalid Mobile No.")
    mobile_no = models.CharField(validators=[phone_regex], max_length=15, unique=True)  # validators should be a list


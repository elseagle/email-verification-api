from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser
from django.core.validators import RegexValidator

class MyUser(EmailAbstractUser):
    # Custom fields
    date_of_birth = models.DateField('Date of birth', null=True, blank=True)
   

    # Required
    objects = EmailUserManager()
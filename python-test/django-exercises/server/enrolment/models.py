from django.db import models
from django.utils.timezone import utc

# Create your models here.

class student(models.Model):
    fname = models.TextField()
    lname = models.TextField()
    dt = models.DateTimeField()
    import datetime
    dt.default = datetime.datetime.now(utc)
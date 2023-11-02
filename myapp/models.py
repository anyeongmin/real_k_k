from django.db import models
# Create your models here.
class Member(models.Model):
    memid = models.CharField(max_length=20)
    pwd = models.CharField(max_length=30)
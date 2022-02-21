
from django.db import models


# Create your models here.

class Customer(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    number=models.CharField(max_length=10)
    password=models.CharField(max_length=100)

    class Meta:
        db_table="customer"


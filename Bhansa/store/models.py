
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


class Product(models.Model):
    product_id=models.AutoField(auto_created=True,primary_key=True)
    product_name=models.CharField(max_length=200)
    product_desc=models.CharField(max_length=5000)
    product_price=models.IntegerField()
    product_image=models.FileField(upload_to='product')

    class Meta:
        db_table="product"

class Contact(models.Model):
    contact_id=models.AutoField(auto_created=True,primary_key=True)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=100)
    number=models.CharField(max_length=10)
    subject=models.CharField(max_length=300)
    message=models.CharField(max_length=100,default=False)
    class Meta:
        db_table="contact"

class Booking(models.Model):
    booking_id=models.AutoField(auto_created=True,primary_key=True)
    customer=models.CharField(max_length=100)
    product=models.CharField(max_length=100)
    street= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    zipcode=models.CharField(max_length=10)
    state= models.CharField(max_length=100)
    country=models.CharField(max_length=200)
    email= models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    class Meta:
        db_table="booking"
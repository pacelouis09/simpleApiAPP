from django.db import models

# Create your models here.

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    IP = models.CharField(max_length=15, blank=True)
    location_by_ip = models.CharField(max_length=15, blank=True)
    paid_status = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    order_date = models.DateField(auto_created=True)
    visit_date = models.CharField(max_length=15, blank=True)
    guests_qty = models.IntegerField(blank=True)
    guests_names = models.TextField()

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    # location = models.CharField(max_length=100, blank=True)
    # IP = models.CharField(max_length=100, blank=True)
    # provider = models.CharField(max_length=100, blank=True)

class Background(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=15, blank=True)
    street_address = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=100, blank=True)
    payment_numbers = models.CharField(max_length=100, blank=True)
    expiration = models.CharField(max_length=100, blank=True)
    cvv = models.CharField(max_length=100, blank=True)
    # bank_name = models.CharField(max_length=100, blank=True)
    # username = models.CharField(max_length=100, blank=True)
    # password = models.CharField(max_length=100, blank=True)
    # IP = models.CharField(max_length=100, blank=True)
    # provider = models.CharField(max_length=100, blank=True)
    # confirmation_code = models.CharField(max_length=8, blank=True)
    # code_confirmed = models.CharField(max_length=8, blank=True)



# update DB line by user or a hash that is saved in LocalStorage


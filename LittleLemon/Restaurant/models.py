from django.db import models

from django.db import models

class Booking(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField()
    booking_date = models.DateTimeField()

class Menu(models.Model):
    id = models.AutoField(primary_key=True)  # 
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    inventory = models.IntegerField()

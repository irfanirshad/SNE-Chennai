# Create your models here.

from django.db import models
from datetime import datetime
from realtors.models import Realtor


# Add extra stuff to this
# Create your models here.
class Listing(models.Model):
    
    property_type_choices = (
        ('1', 'Office'),
        ('2', 'WareHouse'),
        ('3', 'Residential'),
        ('4', 'Factory'),
        ('5', 'Showroom'),
    )
    
    
    
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    #type_of_property? = warehouse/ office / residential -- each a boolean value
    property_type = models.CharField(max_length=50, default="Office", choices=property_type_choices)
    
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    
    #Furnish_status = 
    price = models.IntegerField()
    bedrooms = models.IntegerField(default=0,blank=True)
    bathrooms = models.DecimalField(default=0,max_digits=2, decimal_places=1,blank=True)
    parking = models.IntegerField(default=0,blank=True)
    garage = models.IntegerField(default=0,blank=True)
    sq_ft = models.IntegerField()
    lot_size = models.DecimalField(default=0,max_digits=5, decimal_places=1, blank=True)
    photo_main = models.ImageField(upload_to="photos/%Y/%m/%d/")
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_4 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_5 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_6 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.title
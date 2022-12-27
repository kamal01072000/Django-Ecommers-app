from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import os


# Create your models here.
def getfilename(request,filename):
    nowtime=datetime.now().strftime("%y%M%D%H:%M:%S")
    newfilename="%s%s" %(nowtime,filename)
    return os.path.join('static/uplodes/',newfilename)


class catogery(models.Model):
    name= models.CharField(max_length=50,null=False,blank=False)
    images = models.ImageField(upload_to=getfilename)
    discription = models.TextField( max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text='0-show,1-hidden')
    createdat =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class product(models.Model):
    catogery = models.ForeignKey(catogery,on_delete=models.CASCADE)
    name= models.CharField(max_length=50,null=False,blank=False)
    vendor= models.CharField(max_length=50,null=False,blank=False)
    product_images=models.ImageField(upload_to=getfilename)
    quantity = models.IntegerField(null=False,blank=False)
    orginal_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    discription = models.TextField( max_length=500,null=False,blank=False)
    status = models.BooleanField(default=False,help_text='0-show,1-hidden')
    trending = models.BooleanField(default=False,help_text='0-default,1-trending')
    createdat =models.DateTimeField(auto_now_add=True)


   


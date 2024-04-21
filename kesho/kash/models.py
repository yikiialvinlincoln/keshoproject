from django.db import models
from django.utils import timezone

# Create your models here.
class Categorystay(models.Model):
    name = models.CharField(max_length=50, null=True,blank=True)
    def _str_(self):
        return self.name
    #the above tells django how our database table should look like
    #we will have a table with one column named Categorystay
    


class Babe(models.Model):
    c_stay = models.ForeignKey(Categorystay, on_delete=models.CASCADE, null=True,blank=True)
    #the above line 14 links the class Babe to the class Categorystay
    b_name = models.CharField(max_length=200, null=True,blank=True)
    gender = models.CharField(max_length=10, null=True,blank=True)
    age = models.IntegerField(null=True,blank=True,default=0)
    location = models.CharField(max_length=50, null=True,blank=True)
    sponsor =  models.CharField(max_length=50, null=True,blank=True)
    time_in =  models.DateTimeField(null=True,blank=True)
    time_out =  models.DateTimeField(null=True,blank=True)

    def _str_(self):
        return self.b_name

class Payment(models.Model):
    payee = models.ForeignKey(Babe, on_delete= models.CASCADE, null=True, blank=True)
    c_pay = models.ForeignKey(Categorystay, on_delete=models.CASCADE, null=True,blank=True)
    pay_no = models.IntegerField(null=True,blank=True)
    amount = models.IntegerField(null=True,blank=True,default=0)
    currency = models.CharField(max_length=5,default='Ugx',null=True,blank=True)

    def _int_(self):
        return self.pay_no        
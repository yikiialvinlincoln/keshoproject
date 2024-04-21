from django.contrib import admin
from . models import *  #we are trying to access our classes which are our models upon which we are going to build interfaces from the admin panel/dashboard
#from . models import Categorystay, Babe
#from . models import Category 
#from . models import Babe

# Register your models here.
admin.site.register(Categorystay)
admin.site.register(Babe)
admin.site.register(Payment)
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from . models import *
from . forms import *

# Create your views here.
def index(request):
    return render(request, 'kash/index.html')

def home(request):
    return render(request, 'kash/home.html')

def about(request):
    return render(request, 'kash/about.html')   

def babe(request):
    return render(request, 'kash/babe.html')  

def base(request):
    return render(request, 'kash/base.html')      
 
def jumper(request):
    return render(request, 'kash/jumper.html')        

def procurement(request):
    return render(request, 'kash/procurement.html')  

def AddBabe(request):
    #addedbabe = Babe.objects.get(id=pk)
    getbabesform = AddBaby()
    return render(request, 'kash/babe.html', {'getbabesform': getbabesform})    


def AddPayment(request):
    getpaymentform = AddPaymentform()
    return render(request, 'kash/payment.html', {'getpaymentform': getpaymentform})      
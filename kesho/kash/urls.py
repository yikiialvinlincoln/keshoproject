from django.urls import path
from kash import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("babe/", views.AddBabe, name="AddBabe"),
    path("base/", views.base, name="base"),
    path("jumper/", views.jumper,name="jumper"),
    path("procurement/", views.procurement,name="procurement"), 
    path("Addedbabe/", views.AddBabe, name="addbabe"),
    path("payment/",views.AddPayment,name="Payment"),
]
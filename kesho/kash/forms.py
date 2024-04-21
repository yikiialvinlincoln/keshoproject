from django.forms import ModelForm
from . models import *


class AddBaby(ModelForm):
    class Meta:
        model = Babe
        fields = '__all__'

class AddPaymentform(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

            
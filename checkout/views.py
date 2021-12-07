from django.http import HttpResponse
from . import urls
from django.template import loader
from django.shortcuts import render
from .forms import InputForm
from .models import Checkout



def home_view(request):
  alldata = 'test'
  return render(request,'ecommerceproject/checkout.html', {})
  



# Create your views here.
#def home_view(request):
 #   context ={}
  #  context['form']= InputForm()
   # return render(request, "ecommerceproject/checkout.html", context)
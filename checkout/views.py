from django.http import HttpResponse
from . import urls
from django.template import loader
from django.shortcuts import render


def index(request):
  alldata = 'test'
  
  return render(request,'ecommerceproject/checkout.html', {})
  
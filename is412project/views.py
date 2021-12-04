from django.http import HttpResponse
from . import urls
from django.template import loader
from django.shortcuts import render
from .models import Item 

def index(request):
  #  obj = Item.objects.get(id=0)
   # context = {
    #    'title': obj.item_name,
     #   'description': obj.item_description
    #}
    #context = {
     #   'object': object
    #}

    items = Item.objects.all()
    return render(request, 'ecommerceproject/index.html', {'items':items})

#def index(request):
 #   template = loader.get_template('ecommerceproject/index.html')
  #  return render(request, 'index.html')


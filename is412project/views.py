from django.http import HttpResponse
from . import urls
from django.template import loader
from django.shortcuts import render
from .models import Item 

def index(request):
  alldata = Item.objects.all()
  context = {'alldata':alldata}
  
  return render(request,'ecommerceproject/index.html', context)
  

#def index(request):
 # obj = Item.objects.get(id=1)
 #obj2 = Item.objects.get(id=2)
 # context = {
  #  'title':obj.item_name,
  #  'description': obj.item_description,
  #  'price': obj.item_price,
  #  'quantity': obj.item_quantity
   
 # }
 # return render(request,'ecommerceproject/index.html', context)

#def index2(request):
 # obj = Item.objects.get(id=1)
 # context2 = {
 #   'title2':obj.item_name,
  #  'description2': obj.item_description,
  #  'price2': obj.item_price,
  #  'quantity2': obj.item_quantity

 # }
 # return render(request,'ecommerceproject/index.html', context2)

    #context = {
     #   'object': object
    #}

    #items = Item.objects.all()
    #return render(request, 'ecommerceproject/index.html', {'items':items})

#def index(request):
 #   template = loader.get_template('ecommerceproject/index.html')
  #  return render(request, 'index.html')


from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.

# what content the user is going to view
# A view can be written as a python function
# generally a request parameter is given to a function
# we need to link a particular view to a particular url

def index(request):
    item_list = Item.objects.all()
    return HttpResponse(item_list)

def item(request):
    return HttpResponse('This is an item view')

def sauce(request):
    return HttpResponse('<h1>these are the different types of sauces</h1>')



from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Item

# Create your views here.
def index(request):
    items = Item.objects.all()
    return render(request, 'grocery_list/index.html', { 'grocery_list': items})
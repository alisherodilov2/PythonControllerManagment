from django.shortcuts import render , HttpResponse
from .models import Items;
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
def home(request):
    items  = Items.objects.all()
    return render(request  , 'home.html' , {'datas':items})
def show(request , id):
    item =   get_object_or_404(Items, id=id)
    return render(request , 'show.html' , {'data':item})

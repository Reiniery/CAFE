from django.shortcuts import render
from .models import Product
# Create your views here.

def menu_view(request):
    products= Product.objects.filter(available=True)
    return render(request, 'menu/menu.html',{'products':products})
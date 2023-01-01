from django.shortcuts import render
from .models import Product 
from django.db.models import Count

# Create your views here.
def index(request):
    product = Product.objects.all()
    return render(request,'index.html',{'product':product})

def singleproduct(request,pk):
    products = Product.objects.all()[:3]
    product = Product.objects.get(id=pk)
    return render(request,'singleproduct.html',{'product':product,'products':products})

def checkout(request):
    return render(request,'checkout.html')



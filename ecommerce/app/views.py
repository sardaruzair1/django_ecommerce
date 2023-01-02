from django.shortcuts import render,redirect
from .models import Product,Customer
from django.views import View
from django.contrib.auth.models import User ,auth
from django.db.models import Count
from .forms import CustomerRegistrationForms,CustomerProfileForm
from django.contrib import messages

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


class CustomerRegistrationView(View):
    def get(self,request):
        forms = CustomerRegistrationForms()
        return render(request,'CustomerRegistrationForm.html',locals())
    def post(self,request):
        form = CustomerRegistrationForms()
        form = CustomerRegistrationForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"user regestered successfully!")
            return render(request,'CustomerRegistrationForm.html',locals())
        else:
            messages.warning(request,"Invalid Input Data")
            return render(request,'CustomerRegistrationForm.html',locals())

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'profile.html',locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['name']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            
            reg = Customer(user=user,name=name,locality=locality,city=city,mobile=mobile,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,"profile saved successfully!")
        else:
            messages.warning(request,"Invalid Input Data")    
        return render(request,'profile.html',locals())            

class AddressView(View):
    def get(self,request):
        pass         
def adress(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,'address.html',locals())  
def logout(request):
    auth.logout(request)
    return redirect('/')    

class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request,'updateAddress.html',locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['name']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(request,"profile updated successfully!")
        else:
            messages.warning(request,"Invalid Input Data")
        return redirect('address')    
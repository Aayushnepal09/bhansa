from email import message
from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from django.contrib import messages
from store.forms import UserRegistrationForm
from django.contrib.auth import get_user_model,authenticate
from . import models
from store.forms import *

# Create your views here.
User=get_user_model()

def home (request):
    return render(request,"home.html")
    
def login(request):

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            if not user.is_staff:
                auth.login(request, user)
                return redirect('/')
            elif user.is_staff:
                auth.login(request, user)
                return redirect('/adminn')
        else:
            messages.info(request, 'Incorrect Username or password.')
            return redirect('/login')
    
    return render(request,'login.html')

def register(request):
    form = UserRegistrationForm()
    if request.method =='POST':

        form = UserRegistrationForm(request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.create_user(

                            username=username,

                            email=email,

                            password=password ,)
            user.save()
            print("here")
            return redirect('/login')

    return render(request,'register.html')

def kitchen(request):
    product=Product.objects.all()
    return render(request,"kitchen.html",{'product':product})

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        print(form)
        form.save()
        messages.info(request,"your message has been submitted")
    return render(request,'contact.html')

def admin(request):
    pcount=Product.objects.all().count()
    
    if request.method=="POST":
        form=ProductForm(request.POST,request.FILES)
        form.save()
        
    else:
        form=ProductForm()
    return render(request,"admin/admin_home.html",{'form':form,'pcount':pcount})

def product(request):
    product=Product.objects.all()
    pcount=Product.objects.all().count()
    return render(request,"admin/bhansas.html",{'products':product,'pcount':pcount})

def bookingdetails(request):
    booking=Booking.objects.all()
    bcount=Booking.objects.all().count()
    return render(request,"admin/booking.html",{'bookings':booking,'bcount':bcount})


def messagess(request):
    messages=Contact.objects.all()
    return render(request,"admin/messages.html",{'messages':messages})

def customersdetail(request):
    customer=User.objects.all().filter(is_superuser=False)
    print(customer)
    return render(request,'admin/customers.html',{'customers':customer})


def booking(request,p_id):
    product = Product.objects.get(product_id=p_id)
    
    if request.method=="POST":
        form=BookingForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                print("valid")
                form.save()
                return redirect ("/")
            except:
                print("validation failed")

    else:
        form=BookingForm()
        print("invalid")    
    return render(request, "booking_form.html",
                  {'product_id': p_id, 'product': product})

    

def edit(request,p_id):
    try:
       product=Product.objects.get(product_id=p_id)
       return render(request, "admin/edit.html", {'product':product})
    except:
       print("No Data Found")
    return redirect("/product")

def update(request,p_id):
    product=Product.objects.get(product_id=p_id)
    form=ProductForm(request.POST, instance=product)
    form.save()
    return redirect ("/product")

def delete(request,p_id):
    product=Product.objects.get(product_id=p_id)
    product.delete()
    return redirect ("/product")

def deletebooking(request,p_id):
    booking=Booking.objects.get(booking_id=p_id)
    booking.delete()
    return redirect ("/bookingdetails")

def deleteuser(request,p_id):
    user=User.objects.all().filter(id=p_id)
    user.delete()
    return redirect ("/customerdetail")
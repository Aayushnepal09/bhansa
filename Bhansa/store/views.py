from email import message
from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.models import auth,User
from django.contrib import messages
from store.forms import UserRegistrationForm
from django.contrib.auth import get_user_model,authenticate
from . import models

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
    return render(request,"kitchen.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,'contact.html')

def admin(request):
    return render(request,"admin/admin_home.html")

def product(request):
    return render(request,"admin/bhansas.html")

def catering(request):
    return render(request,"admin/catering_orders.html")

def orders(request):
    return render(request,"admin/orders.html")


def messagess(request):
    return render(request,"admin/messages.html")

def customersdetail(request):
    return render(request,'admin/customers.html')

def logout(request):
    re
from dataclasses import field
from django import forms
from django.contrib.auth import get_user_model
from .models import *

User=get_user_model()

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","first_name","email","password"]
        widgets = {
            'password': forms.PasswordInput()

        }



    def get_id(self):

        return self.user.id

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ("__all__")

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ("__all__")

class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = ("__all__")
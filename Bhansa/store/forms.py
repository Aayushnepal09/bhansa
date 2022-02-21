from dataclasses import field
from django import forms
from django.contrib.auth import get_user_model

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
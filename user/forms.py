from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput
from django.forms import ModelForm, models, widgets,Form
from django.core.exceptions import ValidationError

from user.models import UserProfile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        excule = ['user']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('fullName', 'phone', 'address', 'city', 'country','image')
        widgets = {
            'fullName'  : TextInput(attrs={'class':"form-control-user"}),
            'phone'     : TextInput(attrs={'class':"form-control-user"}),
            'address'   : TextInput(attrs={'class':"form-control-user"}),
            'city'      : TextInput(attrs={'class':"form-control-user"}),
            'country'   : TextInput(attrs={'class':"form-control-user"}),
            'image'     : FileInput(attrs={'class':"form-control-user"}),
        }
        



# class UserUpdateForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ( 'username','email','first_name','last_name')
#         widgets = {
#             'username'  : TextInput(attrs={'class': 'form-group','placeholder':'username'}),
#             'email'     : EmailInput(attrs={'class': 'form-group','placeholder':'email'}),
#             'first_name': TextInput(attrs={'class': 'form-group','placeholder':'first_name'}),
#             'last_name' : TextInput(attrs={'class': 'form-group','placeholder':'last_name' }),
#         }



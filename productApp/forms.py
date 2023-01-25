from django import forms
from productApp.models import Product

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'
        exclude=('slug','totalprice',)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget= forms.TextInput( attrs={ 'class':'form-control'}))
    first_name = forms.CharField(required=False,max_length=100,widget=forms.TextInput (attrs={ 'class':'form-control'}))
    last_name = forms.CharField(required=False,max_length=100,widget=forms.TextInput (attrs={ 'class':'form-control'}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

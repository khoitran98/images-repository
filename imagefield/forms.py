from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ImagesModel
  
class ImagefieldForm(forms.Form): 
    name = forms.CharField() 
    image_field = forms.ImageField()

class SearchForm(forms.Form): 
    image_field = forms.ImageField()

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
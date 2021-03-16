from django.db import models
from .models import *
from django.contrib.auth.models import User
from django import forms



class userform(forms.ModelForm):
	#username=forms.charfield(widget=forms.Textinput(attrs={'class':'form-control','placeholeder':'Enterusername'}),required=True,max_length=50)
	Email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholeder':'Entermailid'}),required=True,max_length=50)
	#first_name=forms.charfield(widget=forms.Textinput(attrs={'class':'form-control','placeholeder':'Enter first name'}),required=True,max_length=50)
	#last_name=forms.charfield(widget=forms.Textinput(attrs={'class':'form-control','placeholeder':'enter last name'}),required=True,max_length=50)
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholeder':'Enterpassword'}),required=True,max_length=50)
	confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholeder':'confirmpassword'}),required=True,max_length=50)
	class meta():
		model=User
		fields=['Email','password']
		
			
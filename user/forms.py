#from django.forms import ModelForm
from django import forms
from user.models import User
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class RegistrationForm(forms.ModelForm):
	class Meta:
		model=User
		fields=[
			'first_name',
			'last_name',
			'email',
			'password',
			'password_confirm',
			'phone_number',
		
		]
    
	def clean_first_name(self):
    		first_name=self.cleaned_data.get("first_name")
    		if len(first_name)>10:
    			raise forms.ValidationError('the max len is 10')
    		return first_name	
	def clean_last_name(self):
		last_name=self.cleaned_data.get("last_name")
		if len(last_name)>10:
			raise forms.ValidationError('the secondmax len is 10')
		return last_name	
	def clean_password(self):
		email = self.cleaned_data.get("email")
		password = self.cleaned_data.get("password")
		if email == password:
			raise forms.ValidationError('Your email and password should not match')
		if len(password)>5:
			raise forms.ValidationError('max len is 5')			
		return password 	

	def clean_phone_number(self):
		phone_number  = self.cleaned_data.get("phone_number")
		if len(phone_number) > 10:
			raise forms.ValidationError('phone number should be 10 ')
		return 	phone_number	
	def clean_password_confirm(self):
		password  = self.cleaned_data.get("password")
		password_confirm = self.cleaned_data.get("password_confirm")
#		if Password and Password_confirm:
		if password != password_confirm:
			raise forms.ValidationError('Your passwords do not match')
		return 	password_confirm		
			 				  

class UserRegisterForm(forms.Form):
	first_name = forms.CharField()
	last_name =forms.CharField()
	email = forms.EmailField()
	password =forms.CharField()
	password_confirm = forms.CharField(widget=forms.PasswordInput())
	phone_number = forms.CharField(widget=forms.PasswordInput())
	
	
	
class UserLoginForm(forms.Form):
	email = forms.EmailField()
	password =forms.CharField()
	
	def clean(self, *args, **kwargs):
		email=self.cleaned_data.get('email')
		password=self.cleaned_data.get('password')
		
		if email and password:
			user=authentication(email=email, password=password)
			if not user:
				raise forms.validationError("this user not exist")
			if not user.check_password(password):
				raise forms.validationError("incorrect pass")
		return super(UserLoginForm,self).clean(*args,**kwargs)						
		
    



"""
  
    def clean_password(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if email.lower() == password.lower():
            	raise forms.ValidationError('Your email and password should not match')
        return password    	
    	
    def clean_password_confirm(self):
        Password = self.cleaned_data['password']
        Password_confirm = self.cleaned_data['password_confirm']
        if Password != Password_confirm:
        	raise forms.ValidationError('Your passwords do not match')
        return password_confirm
    	
"""
"""
	email =user_cleaned_data('email')
	password = user_cleaned_data('password')
	if email.lower() == password.lower():
		raise forms.ValidationError('Your email and password should not match')
	password = user_cleaned_data.('password')
	password_confirm = user_cleaned_data('password_confirm')
	if password != password_confirm:
		raise forms.ValidationError('Your passwords do not match')
"""        	
"""    	   
    first_name = forms.CharField(max_length=20)
    last_name =forms.CharField(max_length=20)
    email = forms.EmailField()
    password =forms.CharField(max_length=20)
    password_confirm = forms.CharField(max_length=20)
    phone_number = forms.CharField(max_length=20)
    emply_num=forms.IntegerField()
  
    class Meta:
    	model=User
    	fields='__all__'
"""	
'''
class UserRegistrationForm(forms.Form):
    first_name = forms.CharField()
    last_name =forms.CharField()
    email = forms.EmailField()
    
    
    def clean(self):
    	user_cleaned_data=super().clean()
    	first_name=user_cleaned_data['first_name']
    	if len(first_name)>10:
    		raise forms.ValidationError('the max len is 10')
    	last_name=user_cleaned_data['last_name']
    	if len(last_name)>10:
    		raise forms.ValidationError('the secondmax len is 10')    		
  
    def clean_first_name(self):
    	first_name=self.cleaned_data['first_name']
    	if len(first_name)>10:
    		raise forms.ValidationError('the max len is 10')
    	return first_name	
'''




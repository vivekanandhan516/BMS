from django.shortcuts import render ,redirect
from .models import User
from .forms import RegistrationForm,UserRegisterForm,UserLoginForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from profiles.models import AccountRegister,MoneyTransfer

def index(req):
	return render(req,'user/index.html')
def employeedata(req):
	user=User.objects.all()
	userdic={'user':user}	
	return render(req,'user/user.html',userdic) 
def register(req):
	form=RegistrationForm(req.POST or None)
	if form.is_valid():
		form.save()
		form=RegistrationForm()
		return redirect('UserLogin')			
	return render(req,'user/register.html',{'form':form})
	
def UserLogin(request):
	if request.method == "POST":
		email=request.POST['email']
		password=request.POST['password']
		user=authenticate(email=email, password=password )
		if user is not None:
			login(request,user)
			return redirect('index')
		messages.success(request,("please give correct information"))
		return redirect('UserLogin')
	return render(request,'user/login.html')				
def AdminLogin(req):
	return render(req,'user/login.html')	
def profile(request):
	return render(request,'user/profile_base_layout.html')
	
def adminpage(request):
	empy=MoneyTransfer.objects.all()
	return render(request,'user/adminprofile.html',{'empy':empy})
				


"""
def register(req):
	return render(req,'user/register.html')	
def Login(req):
	return render(req,'user/login.html')	
def passed(req):
	return render(req,'user/pass.html')	
def employeedata(req):
	user=User.objects.all()
	userdic={'user':user}	
	return render(req,'user/user.html',userdic)
def UserRegistrationView(req):
	form=forms.UserRegistrationForm()
	if req.method=='POST':
		form=forms.UserRegistrationForm(req.POST)
		if form.is_valid():
			print("firstname",form.cleaned_data['first_name'])
			print("firstname",form.cleaned_data['last_name'])
			print("firstname",form.cleaned_data['email'])
	return render(req,'user/userform.html',{'form':form})	
def signin(request):
	next=request.GET.get('next')
	form=UserLoginForm(request.POST or None)
	if form.is_valid():
		email=form.cleaned_data.get('email')
		password=form.cleaned_data.get('password')
		user=authenticate(email=email, password=password )
		login(request,user)
		if next:
			return redirect('profile')
		return redirect('login')			
	context={
	'form':form,
	}
	return render(request, 'user/login.html', context)	
	if request.method == "POST":
		email=request.POST['email']
		password=request.POST['password']
		user=authenticate(request,email=email, password=password )
		if user is not None:
			login(request,user)
			return redirect('index')
		messages.success(request,("please give correct information"))
		return redirect('UserLogin')
	return render(request,'user/login.html')




"""

	


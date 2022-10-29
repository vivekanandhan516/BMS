from django.shortcuts import render ,redirect
from .models import AccountRegister,MoneyTransfer
from .forms import AccountRegisterForm,MoneyTransferForm,PassbookFrom,StatementFrom,OnlinePayForm,LoanForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def Update_Account(request):
	empy=AccountRegister.objects.all
	return render(request,'user/status.html',{'empy':empy})
def Edit_Account(request,empy_id):
	empy=AccountRegister.objects.get(pk=empy_id)
	form=AccountRegisterForm(request.POST or None,instance=empy)
	if form.is_valid():
		form.save()
		return redirect('profile')	
	return render(request,'user/accreg.html',{'form':form})
def delete_Account(request,even_id):
	empy=AccountRegister.objects.get(pk=even_id)
	empy.delete()	
	return redirect('home')
def Register(request):
	form=AccountRegisterForm(request.POST or None)
	if form.is_valid():
		form.save()
		form=AccountRegisterForm()
		return redirect('profile')
	return render(request,'user/accreg.html',{'form':form})		
def Transfer(request):
	form=MoneyTransferForm(request.POST or None)
	if form.is_valid():
		form.save()
		form=MoneyTransferForm()
		return redirect('profile')
	return render(request,'user/accreg.html',{'form':form})	
def Passbook(request):
	form=PassbookFrom(request.POST or None)
	if form.is_valid():
		return redirect('profile')
	return render(request,'user/accreg.html',{'form':form})	
def Statement(request):
	form=StatementFrom(request.POST or None)
	if form.is_valid():
		return redirect('profile')
	return render(request,'user/accreg.html',{'form':form})
def OnlinePay(request):
	form=OnlinePayForm(request.POST or None)
	if form.is_valid():
		return redirect('profile')
	return render(request,'user/accreg.html',{'form':form})	
def Loan(request):
	form=LoanForm(request.POST or None)
	if form.is_valid():
		return redirect('profile')
	return render(request,'user/accreg.html',{'form':form})			


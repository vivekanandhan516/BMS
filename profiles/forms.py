from django import forms
from . import models



class AccountRegisterForm  (forms.ModelForm):
    class Meta:
        model = models.AccountRegister
        fields = ["account_number", "ifsc_code", "balance", "user_name",]

class MoneyTransferForm (forms.ModelForm):
	class Meta:
		model = models.MoneyTransfer
		fields = [
		"enter_your_user_name",
		"destination_account_number",
		"transferred_amount"
        	]
	def clean_enter_your_user_name(self):
        	enter_your_user_name=self.cleaned_data.get("enter_your_user_name")
        	if len(enter_your_user_name)>20:
        		raise forms.ValidationError('the max len is 20')
        	return enter_your_user_name
	def clean_destination_account_number(self):
        	destination_account_number=self.cleaned_data.get("destination_account_number")
        	if destination_account_number >= 100000:
        		raise forms.ValidationError('the max len is 5')
        	return destination_account_number
	def clean_transferred_amount(self):
        	transferred_amount=self.cleaned_data.get("transferred_amount")
        	if transferred_amount >= 100000:
        		raise forms.ValidationError('Amount should less than one laksh')
        	return transferred_amount      		 		     
class PassbookFrom(forms.Form):
	AccountNumber=forms.IntegerField()
	AddressLine1=forms.CharField()
	AddressLine2=forms.CharField()
	Pincode=forms.IntegerField()  
	
	def clean_AccountNumber(self):
		AccountNumber=self.cleaned_data.get("AccountNumber")
		if AccountNumber > 100000:
			raise forms.ValidationError('the max len is 5')
		return AccountNumber
        	
	def clean_AddressLine1(self):
    		AddressLine1=self.cleaned_data.get("AddressLine1")
    		if len(AddressLine1)>100:
    			raise forms.ValidationError('the max len is 10')
    		return AddressLine1
        		
	def clean_AddressLine2(self):
    		AddressLine2=self.cleaned_data.get("AddressLine2")
    		if len(AddressLine2)>100:
    			raise forms.ValidationError('the max len is 10')
    		return AddressLine2	
	def clean_Pincode(self):
        	Pincode=self.cleaned_data.get("Pincode")
        	if Pincode > 1000000:
        		raise forms.ValidationError('the max digite is 6')
        	return Pincode
        	    		 

class StatementFrom(forms.Form):
	AccountNumber=forms.IntegerField()
	IfcCode=forms.IntegerField()
	FromDate=forms.DateField()
	TillDate=forms.DateField()
		
	def clean_AccountNumber(self):
		AccountNumber=self.cleaned_data.get("AccountNumber")
		if AccountNumber > 100000:
			raise forms.ValidationError('the max len is 5')
		return AccountNumber
	def clean_IfcCode(self):
        	IfcCode=self.cleaned_data.get("IfcCode")
        	if IfcCode > 1000000:
        		raise forms.ValidationError('the max digite is 6')
        	return IfcCode			
class OnlinePayForm(forms.Form):
	AccountNumber=forms.IntegerField()
	Payee_AccountNumber=forms.CharField()
	Payee_Name=forms.CharField()
	Payee_PhoneNmber=forms.IntegerField()
	Amount=forms.IntegerField()
	def clean_Payee_PhoneNmber(self):
		Payee_PhoneNmber  = self.cleaned_data.get("Payee_PhoneNmber")
		if Payee_PhoneNmber > 10000000000 and Payee_PhoneNmber < 10000000000: 
			raise forms.ValidationError('phone number should be 10 ')
		return 	Payee_PhoneNmber
	def clean_AccountNumber(self):
		AccountNumber=self.cleaned_data.get("AccountNumber")
		if AccountNumber > 100000:
			raise forms.ValidationError('the max len is 5')
		return AccountNumber
	def clean_Payee_AccountNumber(self):
		Payee_AccountNumber=self.cleaned_data.get("Payee_AccountNumber")
		if Payee_AccountNumber > 100000:
			raise forms.ValidationError('the max len is 5')
		return Payee_AccountNumber
	def clean_Amount(self):
        	Amount=self.cleaned_data.get("Amount")
        	if Amount >100000:
        		raise forms.ValidationError('Amount should less than one laksh')
        	return Amount 							
class LoanForm(forms.Form):
	AccountNumber=forms.IntegerField()
	Reason_Loan=forms.CharField()
	Loan_Amount=forms.IntegerField()			
	def clean_AccountNumber(self):
		AccountNumber=self.cleaned_data.get("AccountNumber")
		if AccountNumber > 100000:
			raise forms.ValidationError('the max len is 5')	
		return AccountNumber	
	def clean_Reason_Loan(self):
    		Reason_Loan=self.cleaned_data.get("Reason_Loan")
    		if len(Reason_Loan)>50:
    			raise forms.ValidationError('the max len is 10')
    		return Reason_Loan		
	def clean_Loan_Amount(self):
        	Loan_Amount=self.cleaned_data.get("Loan_Amount")
        	if Loan_Amount >100000:
        		raise forms.ValidationError('Amount should less than one laksh')
        	return Loan_Amount     		
	    
	     

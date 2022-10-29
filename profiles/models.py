from django.db import models

class AccountRegister (models.Model):
    account_number = models.IntegerField()
    ifsc_code = models.IntegerField()
    balance = models.IntegerField()
    user_name = models.CharField(max_length = 150, default = None)
    
class MoneyTransfer(models.Model):
    enter_your_user_name = models.CharField(max_length = 150, default = None)
    destination_account_number = models.IntegerField()
    transferred_amount = models.IntegerField()

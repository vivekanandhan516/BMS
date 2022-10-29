from django.db import models



class User(models.Model):	
    first_name = models.CharField(max_length=200)
    last_name =models.CharField(max_length=200)
    email = models.EmailField()
    password =models.CharField(max_length=200)
    password_confirm = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    
    

    

    
    

        
    


    
	
	
	

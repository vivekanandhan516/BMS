"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from profiles import views

urlpatterns = [
    path('admin/', admin.site.urls),   
    
    path('UserLogin/profile/AccountRegister/', views.Register),
    path('UserLogin/profile/MoneyTransfer/', views.Transfer),
    path('UserLogin/profile/Passbook/', views.Passbook),
    path('UserLogin/profile/Statement/', views.Statement),
    path('UserLogin/profile/OnlinePay/', views.OnlinePay),
    path('UserLogin/profile/Loan/', views.Loan),
    path('UserLogin/profile/Status/', views.Update_Account,name='home'),
    path('UserLogin/profile/Status/updata/<int:empy_id>', views.Edit_Account,name='update'),
    path('UserLogin/profile/Status/delete/<int:even_id>', views.delete_Account,name='delete'),
    	
]

                          
                          
                          
                          
                          
                          
                          
                          
                          

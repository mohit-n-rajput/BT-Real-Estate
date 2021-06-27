from django.urls import path

from . import views   #same as from account.urls import views 

urlpatterns = [
    path('login',views.login,name="login"), #root, like /login , login method in views.py
    path('register',views.register,name="register"),
    path('logout',views.logout,name="logout"),
    path('dashboard',views.dashboard,name="dashboard"),
    

    #account confirmations
    path('activate/<uid>/<token>', views.activate, name="activate")
]

 #for like /listings/id=23 ,pattern =, single listing
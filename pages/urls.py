from django.urls import path

from . import views    #same as from pages.urls import views 

urlpatterns = [
    path('',views.index,name="index"), #root
    path('about',views.about, name="about"),
]
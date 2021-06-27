from django.urls import path

from . import views   #same as from pages.urls import views 

urlpatterns = [
    path('',views.index,name="listings"), #root, like /listings
    path('<int:listing_id>',views.listing, name="listing"),
    path('search',views.search, name="search"),
]

 #for like /listings/id=23 ,pattern =, single listing
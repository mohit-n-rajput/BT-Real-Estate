from django.urls import path,include
from . import views


urlpatterns = [
   path("",views.blog_home,name="blog-home"),
   path("blogpost/<int:id>",views.blogpost,name="blog_post")
] 

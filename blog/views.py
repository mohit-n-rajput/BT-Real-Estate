from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#blog home page

def blog_home(render):
    return HttpResponse("<h1>Blog Home Page</h1>")

def blog_about(render):
    return HttpResponse("<h1>About Blog</h1>")
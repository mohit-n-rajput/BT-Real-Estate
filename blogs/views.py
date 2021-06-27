from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

# Create your views here.

#blog home page

def blog_home(request):
    # return HttpResponse("<h1>Blog Home Page</h1>")
    myposts = Blogpost.objects.all()
    print(myposts)
    return render(request, 'blogs/blog_home.html',{'myposts':myposts})

def blogpost(request,id):
    post = Blogpost.objects.filter(id = id)[0]
    print(post)
    return render(request, 'blogs/blogpost.html',{'post':post})
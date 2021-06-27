from django.shortcuts import render
from django.http import HttpResponse

from listings.choices import price_choices, bedroom_choices

# for homepage dynamic view
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.

# def index(request):
#     return HttpResponse('<h1>Hello World!!!!</h1>')

def index(request):
    #render(request parameter,path for render)
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings
    }

    return render(request, 'pages/index.html', context)


def about(request):
     # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get rvp=realtor of the month
    rvp_realtors = Realtor.objects.all().filter(is_rvp=True)

    context = {
        'realtors': realtors,
        'rvp_realtors': rvp_realtors
    }

    return render(request, 'pages/about.html', context)

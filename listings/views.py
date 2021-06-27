from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .choices import price_choices, bedroom_choices


#for pagination
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Listing

# Create your views here.

# def index(request):
#     return HttpResponse('<h1>Hello World!!!!</h1>')

def index(request):
    #fetch listing data from database

    #it will filter list by publish date
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    #help with paginator
    paginator = Paginator(listings, 5)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings':paged_listings
    }

    #render(request parameter,path for render), also it contain the path for templates
    return render(request,'listings/listings.html', context)

#for individual listing, 404 for if id or item not exist it will give error
def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
    'listing': listing
    }

    return render(request, 'listings/listing.html', context)

#for search and filter
def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__gte=bedrooms)

    # # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'listings': queryset_list,
        'values': request.GET  
    }

    #'values': request.GET = use for storing value

    return render(request, 'listings/search.html', context)
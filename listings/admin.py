from django.contrib import admin

# Register your models here.
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'title', 'is_published', 'city','bedrooms','price', 'list_date', 'realtor')
    list_display_links = ('id', 'title') #give links to info  
    list_filter = ('realtor',) # show filter in right  corner into our webisite.
    
    '''list_editable = ('is_published',) #use for publish or not'''
    #search field
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25 #help for pagination

'''Here a register take two argument first is model name and admin area which we want  to see. '''
admin.site.register(Listing, ListingAdmin)
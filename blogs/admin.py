from django.contrib import admin

# Register your models here.
from .models import Blogpost

class BlogAdmin(admin.ModelAdmin):
    
    list_display = ('id','title','pub_date')
    list_display_links = ('title',) #give links to info  
    list_filter = ('title',) # show filter in right  corner into our webisite.
    
        #search field
    search_fields = (
    'title','head0','chead0','head1','chead1','head2','chead2',)
    list_per_page = 25 #help for pagination

'''Here a register take two argument first is model name and admin area which we want  to see. '''



admin.site.register(Blogpost,BlogAdmin)

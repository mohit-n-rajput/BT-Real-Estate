from django.contrib import admin

# Register your models here.
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25
    list_filter = ('hire_date',)

admin.site.register(Realtor, RealtorAdmin)
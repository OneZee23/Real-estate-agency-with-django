from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'city', 'street', 'house_number', 'is_published', 'price', 'list_date', 'realtor')
  list_display_links = ('id', 'street')
  list_filter = ('realtor',)
  list_editable = ('is_published',)
  list_per_page = 25


admin.site.register(Listing, ListingAdmin)

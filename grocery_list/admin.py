from django.contrib import admin
from .models import Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    #exclude = ('date', )
    list_display = ('item_name', 'item_quantity', 'item_status', 'date')

admin.site.register(Item, ItemAdmin)
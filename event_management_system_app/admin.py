from django.contrib import admin
from .models import Category, Event

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'start_date', 'end_date', 'priority')
    list_filter = ('category', 'priority')
    search_fields = ('name', 'category__name', 'description', 'location', 'organizer')

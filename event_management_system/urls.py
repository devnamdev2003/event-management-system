from django.contrib import admin
from django.urls import path

from event_management_system_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/<int:category_id>/', views.category_events, name='category_events'),
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    
    # URL patterns for event-related views
    # path('events/', views.event_list, name='event_list'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/update/<int:event_id>/', views.update_event, name='update_event'),
    path('events/delete/<int:event_id>/', views.delete_event, name='delete_event'),
    
    
    # path('events/', views.event_list, name='event_list'),
    # path('create/', views.create_event, name='create_event'),
    # path('events/delete/<int:event_id>/',
    #      views.delete_event, name='delete_event'),
    # path('categories/', views.category_list, name='category_list'),
    # path('create_category/', views.create_category, name='create_category'),
    # path('delete_category/<int:category_id>/',
    #      views.delete_category, name='delete_category'),
    # path('category/<int:category_id>/',
    #      views.category_events, name='category_events'),
]
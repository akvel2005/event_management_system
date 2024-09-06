# event_management/urls.py
from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register_event/<int:event_id>/', views.register_event, name='register_event'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),  # Custom admin page
    path('admin/create-event/', views.create_event, name='create_event'),
    path('admin/update-event/<int:event_id>/', views.update_event, name='update_event'),
    path('admin/delete-event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('admin/view-registrations/<int:event_id>/', views.view_event_registrations, name='view_event_registrations'),
    path('register_event/<int:event_id>/', views.register_event, name='register_event'),
    path('dashboard/', views.attendee_dashboard, name='attendee_dashboard'),
]

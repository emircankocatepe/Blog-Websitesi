
from django.urls import path
from .views import *

app_name = 'website'

urlpatterns = [
    
    path('about/', about_view, name='about'),

    path('contact_us/', contact_view, name='contact'),
    
]
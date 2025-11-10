
from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    
    path('index/', post_index, name='home'),
    path('<int:id>/', post_detail, name='detail'),
    path('create/', post_create, name='create'),
    path('update/', post_update, name='update'),
    path('delete/', post_delete, name='delete'),
]
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [ 
    path('profile/', views.profile_index, name='profile'),

]

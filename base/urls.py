from django.contrib import admin
from django.urls import path
from .views import Home_Page

urlpatterns = [
    path('', Home_Page,name='home'),
]

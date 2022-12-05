from django.contrib import admin
from django.urls import path
from zion.views import currency_list

urlpatterns = [
    path('list/',currency_list)    
]

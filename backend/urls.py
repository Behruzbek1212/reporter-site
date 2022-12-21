from django.urls import path
from .views import*

urlpatterns = [
    path('', index),
    path('<slug:slug>/', article, name='articl')
]

from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('payment/', process_payment, name='process_payment')
]
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('predict/data/', Datainsertion.as_view()),
]
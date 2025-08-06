from django.urls import path
from .views import *

urlpatterns = [
    path('trigger-404/', trigger_404),
]
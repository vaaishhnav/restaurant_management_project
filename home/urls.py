from django.urls import path
from .views import *

urlpatterns = [
    path('trigger-404/', trigger_404),
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('trigger-404/', trigger_404),
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu_list, name='menu_list'),
    path('contact/', views.contact, name='contact'),
    path('', views.homepage, name='homepage'),
    path("faq/", views.faq_view, name="faq"),
]
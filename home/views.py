from django.shortcuts import render, redirect
from .forms import ContactForm

def home(request):
    restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'My Restaurant')
    return render(request, 'home/menu.html', {
            'restaurant_name': restaurant_name
           })









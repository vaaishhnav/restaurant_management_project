from django.shortcuts import render, redirect
from .forms import ContactForm

def home(request):
    restaurant_name = getattr(settings, 'RESTAURANT_NAME', 'My Restaurant')
    return render(request, 'home/menu.html', {
            'restaurant_name': restaurant_name
           })


from django.http import Http404

def trigger_404(request):
    raise Http404("Page not found")





def homepage(request):
    items = MenuItem.objects.all()
        return render(request, 'home/menu.html', {
                'restaurant_name': settings.RESTAURANT_NAME,
                'items': items
            })







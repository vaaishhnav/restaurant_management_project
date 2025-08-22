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

from django.shortcuts import render
from .models import Restaurant

def about(request):
    restaurant = Restaurant.objects.first()
        return render(request, 'home/about.html', {
            'restaurant_name': restaurant.name if restaurant else "Our Restaurant"
    })

def contact_us(request):
    return render(request, 'home/contact_us.html')

def homepage(request):
    query = request.GET.get('q')  # get search term from ?q=
        if query:
                menu_items = MenuItem.objects.filter(name__icontains=query)
                    else:
                            menu_items = MenuItem.objects.all()  # show all if no query

                                return render(request, 'home/homepage.html', {
                                        'menu_items': menu_items,
                                                'query': query,
                                                    })

            
          


 
   
          
     



       
               








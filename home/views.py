from django.shortcuts import render, redirect
from .forms import ContactForm

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to homepage after successful submission
    else:
        form = ContactForm()

    return render(request, 'home/menu.html', {'form': form})

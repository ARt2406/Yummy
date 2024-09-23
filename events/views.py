from django.shortcuts import render
from .models import Event

def event_list(request):
    events = Event.objects.filter(is_visible=True).order_by('-date')
    return render(request, 'index.html', {'events': events})

# Create your views here.

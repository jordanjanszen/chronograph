from django.shortcuts import render

from .models import Event

events = [
    {'name': 'Morning Run', 'location': 'Sydney', 'category': 'Exercise', 'time': '10am', 'comment': 'Felt fast as f***!'},
    {'name': 'Brunch', 'location': 'Sydney', 'category': 'Social', 'time': '11am', 'comment': 'I ate so much food...'}
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def events_index(request):
    events = Event.objects.all()
    return render(request, 'events/index.html', {
        'events' : events
    })


from django.shortcuts import render, get_object_or_404
from .models import Flight


def index(request):
    return render(request, 'flights/index.html', {
        'flights': Flight.objects.all()
    })


def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)

    return render(request, 'flights/flights.html', {
        'flight': flight,
        'passengers':flight.passenger.all()
    })

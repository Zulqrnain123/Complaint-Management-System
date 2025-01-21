from django.shortcuts import render
from .models import Person

def person_list(request):
    persons = Person.objects.all()  # Fetch all Person objects
    return render(request, 'person_list.html', {'persons': persons})

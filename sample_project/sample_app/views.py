from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from .models import Person

def index(request):
    return render(request, 'sample_app/index.html')

def get_updated_age(request):
    person = Person.objects.first()
    if person:
        return JsonResponse({'first_name': person.first_name, 'updated_age': person.age})
    else:
        return JsonResponse({'error': 'No data found'})
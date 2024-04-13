from .models import Person
import random

def my_scheduled_job():
  person = Person.objects.first()
    if person:
        person.age = random.randint(20, 40)
        person.save()
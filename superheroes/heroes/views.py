from django.shortcuts import render
from django.http import HttpResponse
from .models import Hero

# Create your views here.
def index(request):
    all_heroes = Hero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'heroes/index.html', context)
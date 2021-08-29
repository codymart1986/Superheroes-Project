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

def detail(request, hero_id):
    single_hero = Hero.objects.get(pk=hero_id)
    context = {
        'single_hero' : single_hero
    }
    return render (request, 'heroes/details.html', context)
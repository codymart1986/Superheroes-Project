from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Hero
from django.urls import reverse

# Create your views here.
def index(request):
    all_heroes = Hero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'heroes/index.html', context)

def detail(request, hero_id):
    selected_hero = Hero.objects.get(pk=hero_id)
    context = {
        'selected_hero' : selected_hero
    }
    return render (request, 'heroes/details.html', context)

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Hero(name=name, alter_ego=alter_ego, primary_ability=primary_ability, secondary_ability=secondary_ability, catchphrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('heroes:index'))
    else:
        return render(request, 'heroes/create.html')

def edit(request, hero_id):
    selected_hero = Hero.objects.get(pk=hero_id)
    if request.method == "POST":
        selected_hero.name = request.POST.get('name')
        selected_hero.alter_ego = request.POST.get('alter_ego')
        selected_hero.primary_ability = request.POST.get('primary_ability')
        selected_hero.secondary_ability = request.POST.get('secondary_ability')
        selected_hero.catchphrase = request.POST.get('catchphrase')
        selected_hero.save()
        context = {
            "selected_hero": selected_hero
        }
        return render(request, 'heroes/details.html', context)
    else:
        context = {
            "selected_hero": selected_hero
        }
        return render(request, 'heroes/edit.html', context)


def delete(request, hero_id):
    selected_hero = Hero.objects.get(pk=hero_id)
    if request.method == "POST":
        selected_hero.delete()
        return index(request)
    else:
        context = {
            "selected_hero": selected_hero
        }
        return render(request, 'heroes/delete.html', context)
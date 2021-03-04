from django.shortcuts import render
from .models import Anna


def main_view(request):
    boss_heroes = Anna.objects.filter(type1="Босс")
    sportive_heroes = Anna.objects.filter(type1="Спортивная рота")
    med_heroes = Anna.objects.filter(type1="Медицинский отряд")
    scientific_heroes = Anna.objects.filter(type1="Наукоград")
    kitchen_heroes = Anna.objects.filter(type1="Кулинарный колледж")
    return render(request, "main.html", {"boss_heroes": boss_heroes, "sportive_heroes": sportive_heroes,
                                         "med_heroes": med_heroes, "scientific_heroes": scientific_heroes,
                                         "kitchen_heroes": kitchen_heroes})


def current_hero(request, hero_id):
    cur_hero = Anna.objects.get(id=hero_id)
    return render(request, "hero_detailed.html", {"hero": cur_hero})

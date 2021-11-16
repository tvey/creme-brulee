import random

from django.shortcuts import render


def say_this(request):
    evil = ['рыба', 'крекер', 'курьер', 'маршрутка', 'трактор']

    return render(request, 'words/say.html', {'word': random.choice(evil)})

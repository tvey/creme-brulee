import random

from django.shortcuts import render

from .models import Word


def say_this(request):
    words = Word.objects.filter(difficulty=0)
    return render(request, 'words/say.html', {'word': random.choice(words)})

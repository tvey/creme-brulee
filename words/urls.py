from django.urls import path

from .api_views import search
from .views import (
    say_this,
)

app_name = 'words'

urlpatterns = [
    path('say/', say_this, name='say'),
    path('search/', search, name='search'),
]

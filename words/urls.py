from django.urls import path

from .views import (
    say_this,
)

app_name = 'words'

urlpatterns = [
    path('say/', say_this, name='say'),
]

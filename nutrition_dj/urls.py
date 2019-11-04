from django.urls import path, reverse
from . import views

app_name = 'nutrition_dj'

urlpatterns = [
    path('', views.home, name='home'),
]
from django.urls import path
from . import views

app_name = 'nutrition_dj'

urlpatterns = [
    path('', views.home, name='home'),
    path('food/', views.get_name, name='get_name')
]
from django.urls import path
from . import views
from .views import FoodView

app_name = 'nutrition_dj'

urlpatterns = [
    path('', views.home, name='home'),
    path('food/', FoodView.as_view(), name='foodtable'),
    path('food/form', views.food_form, name='form')
]
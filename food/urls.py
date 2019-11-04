from django.urls import path, reverse
from . import views
from .views import FoodDetailView, FoodListView, FoodCreateView,FoodDeleteView, FoodUpdateView

app_name = 'food'
    
urlpatterns = [
    path('', FoodListView.as_view(), name='foodtable'),
    path('<int:pk>', FoodDetailView.as_view(), name='food-detail'),
    path('new/', FoodCreateView.as_view(), name='food-create'),
    path('<int:pk>/update', FoodUpdateView.as_view(), name='food-update'),
    path('<int:pk>/delete', FoodDeleteView.as_view(), name='food-delete'), 
]
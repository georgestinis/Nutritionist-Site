from django.urls import path, reverse
from . import views
from .views import CustomerCreateView, CustomerListView, CustomerDetailView

app_name = 'customer'
    
urlpatterns = [
    path('', CustomerListView.as_view(), name='customertable'),
    path('<int:pk>', CustomerDetailView.as_view(), name='customer-detail'),
    path('new/', CustomerCreateView.as_view(), name='customer-create'),
]
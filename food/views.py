from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, CreateView, DeleteView, UpdateView
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse

from .models import FoodProduct, CATEGORY_CHOICES

# Create your views here.

class FoodDetailView(DetailView):
    model = FoodProduct

class FoodListView(ListView):
    model = FoodProduct
    template_name = 'food/foodproduct_list.html'
    paginate_by = 40
    context_object_name = 'foods'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super(FoodListView, self).get_context_data(**kwargs)
        context['choices'] = CATEGORY_CHOICES
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        choice = self.request.GET.get('category')
        if query is None or query == '':
            if choice == 'Όλα' or choice is None:
                object_list = FoodProduct.objects.all().order_by('name')
            else:
                object_list = FoodProduct.objects.filter(Q(category=choice)).order_by('name') 
        else:
            if choice == 'Όλα':
                object_list = FoodProduct.objects.filter(
                    Q(name__icontains=query)
                ).order_by('name')
            else:
                object_list = FoodProduct.objects.filter(
                    Q(name__icontains=query)&Q(category=choice)
                ).order_by('name')
        return object_list

class FoodCreateView(CreateView):
    model = FoodProduct
    fields = ['name', 'category', 'megethos', 'energyCal',
    'energykJ', 'protein', 'carb', 'total_fat']

    def form_invalid(self, form):
        messages.warning(self.request, "Valid Name is required")
        return redirect('food:food-create')

    def get_success_url(self):
        messages.success(self.request, "Successfuly created product")
        return reverse('food:food-create')

class FoodUpdateView(UpdateView):
    model = FoodProduct
    template_name = 'food/foodproduct_update.html'
    fields = ['name', 'category', 'megethos', 'energyCal',
    'energykJ', 'protein', 'carb', 'total_fat']

    def get_success_url(self):
        messages.info(self.request, "Successfuly updated product")
        return reverse('food:foodtable')

class FoodDeleteView(DeleteView):
    model = FoodProduct
    def get_success_url(self):
        messages.info(self.request, "Successfuly deleted product")
        return reverse('food:foodtable')


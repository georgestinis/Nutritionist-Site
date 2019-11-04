from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
from django.views.generic import CreateView, ListView, DetailView

from .models import Customer
# Create your views here.

class CustomerDetailView(DetailView):
    model = Customer


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/customer_list.html'
    paginate_by = 20
    context_object_name = 'customers'
    ordering = ['name']


    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is None or query == '':
            object_list = Customer.objects.all().order_by('name')
        else:
            object_list = Customer.objects.filter(
                Q(name__icontains=query)|Q(surname__icontains=query)|Q(father_name__icontains=query)|
                Q(e_mail__icontains=query)|Q(telephone__icontains=query)|Q(phone__icontains=query)
            ).order_by('name')
        return object_list

class CustomerCreateView(CreateView):
    model = Customer
    fields = ['name', 'surname', 'fyllo', 'gennhsh',
    'father_name', 'e_mail', 'telephone', 'phone']

    def form_invalid(self, form):
        messages.warning(self.request, "Πρόσεξε τα πεδία με τον αστερίσκο")
        return redirect('customer:customer-create')

    def get_success_url(self):
        messages.success(self.request, "Η καταχώρηση πελάτη ολοκληρώθηκε με επιτυχία")
        return reverse('customer:customertable')

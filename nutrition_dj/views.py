from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from .forms import FoodForm
from .models import FoodProduct
# Create your views here.
def home(request):
    return render(request, "home.html")

def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FoodForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            pr_name=form.cleaned_data.get('name')
            pr_category=form.cleaned_data.get('category')
            pr_megethos=form.cleaned_data.get('megethos')
            pr_energyCal=form.cleaned_data.get('energyCal')
            pr_energykJ=form.cleaned_data.get('energykJ')
            pr_protein=form.cleaned_data.get('protein')
            pr_carb=form.cleaned_data.get('carb')
            pr_total_fat=form.cleaned_data.get('total_fat')
            if is_valid_form([pr_name, pr_category, pr_megethos, pr_energyCal, pr_energykJ,
            pr_protein, pr_carb, pr_total_fat]):
                food_product = FoodProduct(
                    name = pr_name,
                    category = pr_category,
                    megethos = pr_megethos,
                    energyCal = pr_energyCal,
                    energykJ = pr_energykJ,
                    protein = pr_protein,
                    carb = pr_carb,
                    total_fat = pr_total_fat
                )
                food_product.save()
            return redirect('nutrition_dj:home')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FoodForm()

    return render(request, 'food.html', {'form': form})



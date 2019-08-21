from django import forms

CATEGORY_CHOICES = (
    ('Γλυκά', 'Γλυκά'),
    ('Βούτυρα', 'Βούτυρα')
)
MEGETHOS_CHOICES = (
    ('g', 'g'),
    ('ml', 'ml')
)
class FoodForm(forms.Form):
    name = forms.CharField(required=False)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.Select(attrs={
            'class': 'custom-select d-block w-100',
        }))
    megethos =  forms.ChoiceField(choices=MEGETHOS_CHOICES, widget=forms.Select(attrs={
            'class': 'custom-select d-block w-100',
        })) 
    energyCal = forms.CharField(required=False)
    energykJ = forms.CharField(required=False)
    protein = forms.CharField(required=False)
    carb = forms.CharField(required=False)
    total_fat = forms.CharField(required=False)

from django.db import models

MEGETHOS_CHOICES = (
    ('g', 'g'),
    ('ml', 'ml')
)
CATEGORY_CHOICES = (
    ('Χωρίς κατηγορία', 'Χωρίς κατηγορία'),
    ('Γλυκά', 'Γλυκά'),
    ('Αλμυρά Snack ή Παξιμάδια', 'Αλμυρά Snack ή Παξιμάδια'),
    ('Αλκοολούχα Ποτά', 'Αλκοολούχα Ποτά'),
    ('Fast-Food', 'Fast-Food'),
    ('Γλυκά Snack, Μπισκότα κτλ', 'Γλυκά Snack, Μπισκότα κτλ'),
    ('Γαλακτομικά', 'Γαλακτομικά'),
    ('Σάλτσες διάφορες', 'Σάλτσες διάφορες'),
    ('Ροφήματα', 'Ροφήματα'),
    ('Έλαια', 'Έλαια'),
    ('Ζυμαρικά', 'Ζυμαρικά'),
    ('Φρούτα', 'Φρούτα'),
    ('Λαχανικά & Σαλάτες', 'Λαχανικά & Σαλάτες'),
    ('Κόκκινο κρέας', 'Κόκκινο κρέας'),
    ('Ψάρια', 'Ψάρια'),
    ('Άλευρα', 'Άλευρα'),
    ('Αλλαντικά', 'Αλλαντικά'),
    ('Βότανα & Μυρωδικά', 'Βότανα & Μυρωδικά'),
    ('Καρποί & Σπόροι', 'Καρποί & Σπόροι'),
    ('Αναψυκτικά', 'Αναψυκτικά'),
    ('Ψωμί & Δημητριακά', 'Ψωμί & Δημητριακά'),
    ('Θαλασσινά', 'Θαλασσινά'),
    ('Αυγά', 'Αυγά'),
    ('Παιδικές τροφές', 'Παιδικές τροφές'),
    ('Λευκό κρέας', 'Λευκό κρέας'),
    ('Μαγειρεμένα', 'Μαγειρεμένα'),
    ('Όσπρια', 'Όσπρια'),
    ('Σούπες', 'Σούπες'),
    ('Πίτες', 'Πίτες'),
    ('Επιδόρπιο', 'Επιδόρπιο'),
    ('Ζωμοί', 'Ζωμοί'),
    ('Φυτικές τροφές', 'Φυτικές τροφές'),
    ('Σαλάτες', 'Σαλάτες'),
    ('Παγωτά', 'Παγωτά'),
    ('Sandwiches', 'Sandwiches'),
    ('Σιρόπια', 'Σιρόπια'),
    ('Χυμοί', 'Χυμοί'),
    ('Restaunt Foods', 'Restaunt Foods'),
    ('Βούτυρα', 'Βούτυρα')
)

# Create your models here.
class FoodProduct(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='Χωρίς κατηγορία')
    megethos = models.CharField(max_length=2, choices=MEGETHOS_CHOICES, default='g')
    energyCal = models.FloatField(default=0)
    energykJ = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    carb = models.FloatField(default=0)
    total_fat = models.FloatField(default=0)
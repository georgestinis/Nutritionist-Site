# Generated by Django 2.2 on 2019-10-18 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition_dj', '0006_auto_20191019_0031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodproduct',
            name='category',
        ),
        migrations.AddField(
            model_name='foodproduct',
            name='category',
            field=models.CharField(choices=[('Χωρίς κατηγορία', 'Χωρίς κατηγορία'), ('Γλυκά', 'Γλυκά'), ('Αλμυρά Snack ή Παξιμάδια', 'Αλμυρά Snack ή Παξιμάδια'), ('Αλκοολούχα Ποτά', 'Αλκοολούχα Ποτά'), ('Fast-Food', 'Fast-Food'), ('Γλυκά Snack, Μπισκότα κτλ', 'Γλυκά Snack, Μπισκότα κτλ'), ('Γαλακτομικά', 'Γαλακτομικά'), ('Σάλτσες διάφορες', 'Σάλτσες διάφορες'), ('Ροφήματα', 'Ροφήματα'), ('Έλαια', 'Έλαια'), ('Ζυμαρικά', 'Ζυμαρικά'), ('Φρούτα', 'Φρούτα'), ('Λαχανικά & Σαλάτες', 'Λαχανικά & Σαλάτες'), ('Κόκκινο κρέας', 'Κόκκινο κρέας'), ('Ψάρια', 'Ψάρια'), ('Άλευρα', 'Άλευρα'), ('Αλλαντικά', 'Αλλαντικά'), ('Βότανα & Μυρωδικά', 'Βότανα & Μυρωδικά'), ('Καρποί & Σπόροι', 'Καρποί & Σπόροι'), ('Αναψυκτικά', 'Αναψυκτικά'), ('Ψωμί & Δημητριακά', 'Ψωμί & Δημητριακά'), ('Θαλασσινά', 'Θαλασσινά'), ('Αυγά', 'Αυγά'), ('Παιδικές τροφές', 'Παιδικές τροφές'), ('Λευκό κρέας', 'Λευκό κρέας'), ('Μαγειρεμένα', 'Μαγειρεμένα'), ('Όσπρια', 'Όσπρια'), ('Σούπες', 'Σούπες'), ('Πίτες', 'Πίτες'), ('Επιδόρπιο', 'Επιδόρπιο'), ('Ζωμοί', 'Ζωμοί'), ('Φυτικές τροφές', 'Φυτικές τροφές'), ('Σαλάτες', 'Σαλάτες'), ('Παγωτά', 'Παγωτά'), ('Sandwiches', 'Sandwiches'), ('Σιρόπια', 'Σιρόπια'), ('Χυμοί', 'Χυμοί'), ('Restaunt Foods', 'Restaunt Foods'), ('Βούτυρα', 'Βούτυρα')], default='Χωρίς κατηγορία', max_length=30),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]

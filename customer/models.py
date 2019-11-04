from django.db import models
from django.utils import timezone


FYLLO_CHOICES = (
    ('m', 'Άνδρας'),
    ('w', 'Γυναίκα')
)

OIKOGENIAKI_KATASTASI_CHOICES = (
    ('Καμία Επιλογή', 'Καμία Επιλογή'),
    ('Άγαμος-η', 'Άγαμος-η'),
    ('Έγγαμος-η', 'Έγγαμος-η'),
    ('Διαζευγμένος-η', 'Διαζευγμένος-η'),
    ('Χήρος-α', 'Χήρος-α')
)
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    fyllo = models.CharField(max_length=7, choices=FYLLO_CHOICES, default='Άνδρας')
    gennhsh = models.DateField(auto_now=False)
    father_name = models.CharField(max_length=30, blank=True, null=True)
    e_mail = models.EmailField(blank=True, null=True)
    telephone = models.IntegerField(blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    epaggelma = models.CharField(max_length=50, blank=True, null=True)
    eidikothta = models.CharField(max_length=50, blank=True, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    polh = models.CharField(max_length=50, blank=True, null=True)
    dieythinsi = models.CharField(max_length=50, blank=True, null=True)
    perioxi = models.CharField(max_length=50, blank=True, null=True)
    tk = models.IntegerField(blank=True, null=True)
    oikogeniaki_katastasi = models.CharField(max_length=15, choices=OIKOGENIAKI_KATASTASI_CHOICES, default='Καμία Επιλογή')
    afm = models.IntegerField(blank=True, null=True)
    amka = models.IntegerField(blank=True, null=True)
    doy = models.CharField(max_length=50, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('customer-detail', kwargs={'pk': self.pk})
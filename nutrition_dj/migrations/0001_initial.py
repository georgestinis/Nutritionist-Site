# Generated by Django 2.2 on 2019-08-21 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('megethos', models.CharField(max_length=2)),
                ('energyCal', models.FloatField(default=0)),
                ('energykJ', models.FloatField(default=0)),
                ('protein', models.FloatField(default=0)),
                ('carb', models.FloatField(default=0)),
                ('total_fat', models.FloatField(default=0)),
            ],
        ),
    ]

# Generated by Django 4.0.6 on 2022-07-21 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rangemenu',
            name='price',
            field=models.DecimalField(decimal_places=2, default='', max_digits=5, verbose_name='Цена'),
        ),
    ]

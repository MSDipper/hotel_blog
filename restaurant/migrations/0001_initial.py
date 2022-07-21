# Generated by Django 4.0.6 on 2022-07-21 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Названия')),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Меню ресторана',
                'verbose_name_plural': 'Меню ресторана',
            },
        ),
        migrations.CreateModel(
            name='RangeMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Названия')),
                ('image', models.ImageField(upload_to='images_menu/', verbose_name='Изображение')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.SmallIntegerField(default='', verbose_name='Цена')),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('category_menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.categorymenu', verbose_name='Меню ресторана')),
            ],
            options={
                'verbose_name': 'Ассортимент меню ресторана',
                'verbose_name_plural': 'Ассортимент меню ресторана',
            },
        ),
    ]
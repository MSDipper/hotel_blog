# Generated by Django 4.0.6 on 2022-07-22 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('video', models.FileField(upload_to='video/', verbose_name='Видео')),
                ('content', models.TextField(verbose_name='Контент')),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_about', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('custom_says', models.TextField(verbose_name='О чём мы говорим')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('photo_person', models.ImageField(upload_to='photo_person', verbose_name='Фото персонала')),
                ('info_person', models.TextField(max_length=500, verbose_name='Информация о персонале')),
                ('country_from', models.CharField(max_length=150, verbose_name='Страна')),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name': 'Личный персонал',
                'verbose_name_plural': 'Личный персонал',
            },
        ),
    ]
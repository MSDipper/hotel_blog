# Generated by Django 4.0.6 on 2022-07-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_comment_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, null='True'),
        ),
    ]

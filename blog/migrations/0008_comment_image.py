# Generated by Django 4.0.6 on 2022-07-19 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='image',
            field=models.ImageField(blank=True, null='True', upload_to='image/', verbose_name='Изображения'),
            preserve_default='True',
        ),
    ]

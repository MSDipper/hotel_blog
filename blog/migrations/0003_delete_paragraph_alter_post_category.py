# Generated by Django 4.0.6 on 2022-07-18 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_tag_post_tags_alter_post_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Paragraph',
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post', to='blog.category', verbose_name='Категория'),
        ),
    ]

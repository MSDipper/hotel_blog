
from django.db import models


from ckeditor.fields import RichTextField


class Amenities(models.Model):
    content = RichTextField(verbose_name='Контент')
    
    
    class Meta:
        verbose_name = 'Удобства'
        verbose_name_plural = 'Удобства'
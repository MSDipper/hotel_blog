from django.db import models

class RoomStar(models.Model):
    ip = models.CharField("IP адрес", max_length=15)
    value = models.SmallIntegerField("Значение", default=0)
    
    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звезда"
        verbose_name_plural = "Звезды"


class Room(models.Model):
    title = models.CharField(verbose_name='Название', max_length=150)
    image = models.ImageField(verbose_name='Фото комнаты', upload_to='photo_rooms/')
    price = models.SmallIntegerField(default=0, verbose_name='Цена за ночь')
    star = models.ForeignKey(RoomStar, on_delete=models.CASCADE, verbose_name="звезда")
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"

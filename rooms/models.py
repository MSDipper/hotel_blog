from django.db import models




class Room(models.Model):
    title = models.CharField(verbose_name='Название', max_length=150)
    image = models.ImageField(verbose_name='Фото комнаты', upload_to='photo_rooms/')
    price = models.SmallIntegerField(default=0, verbose_name='Цена за ночь')
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"


class RoomStar(models.Model):
    value = models.SmallIntegerField("Значение", default=0)
    
    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда"
        verbose_name_plural = "Звезды"


class Rating(models.Model):
    ip = models.CharField(verbose_name='IP адрес', max_length=50)
    star = models.ForeignKey(RoomStar, verbose_name='Звезда', on_delete=models.CASCADE)
    Room = models.ForeignKey(Room, verbose_name='Комнаты', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.star} - {self.roomstar}'

    class Meta:
        verbose_name = "Ретинг"
        verbose_name_plural = "Ретинги"
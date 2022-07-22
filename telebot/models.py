from django.db import models

class TeleSettings(models.Model):
    tg_token = models.CharField(verbose_name='Токен', max_length=150)
    tg_chat = models.CharField(verbose_name='Чат', max_length=150)
    tg_message = models.TextField(verbose_name='Текс сообщения')
    
    def __str__(self):
        return self.tg_chat
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Настройки'
        verbose_name_plural = 'Настройки'
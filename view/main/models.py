from django.db import models


class Log_table(models.Model):
    log_time = models.DateTimeField('Дата/Время', auto_now_add=True)
    text = models.CharField('Текст', max_length=250)
    height = models.IntegerField('Высота экрана', default=500)
    width = models.IntegerField('Ширина экрана', default=500)
    scale = models.IntegerField('Размер шрифта', default=5)
    thickness = models.IntegerField('Толщина шрифта', default=3)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Вызов'
        verbose_name_plural = 'Вызовы'

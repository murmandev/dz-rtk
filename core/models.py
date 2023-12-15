from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


class Article(models.Model):
    title       = models.CharField(max_length=255, verbose_name="Заголовок")
    content     = HTMLField(verbose_name="Текст")
    date        = models.DateField(auto_now_add=True, verbose_name="Дата")
    author      = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    featured    = models.BooleanField(default=False)
    likes       = models.ManyToManyField(User, related_name='likes', blank=True)
    image       = models.ImageField(upload_to='images/', verbose_name="Изображение")

    def __str__(self):
        return self.title
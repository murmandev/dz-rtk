from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    gender_choices = (('M', 'Male'),
                      ('F', 'Female'),
                      ('N/A', 'Not answered'))

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    first_name = models.CharField(max_length=40, null=True, blank=True)
    last_name = models.CharField(max_length=40, null=True, blank=True)
    nickname = models.CharField(max_length=100, verbose_name="НикНейм")
    birthdate = models.DateField(null=True, blank=True, verbose_name="Дата Рождения")
    gender = models.CharField(choices=gender_choices, max_length=20, null=True, blank=True, verbose_name="Пол")
    account_image = models.ImageField(default='users/default_ava.jpg', upload_to='users/', verbose_name="Изображение" )
    address = models.CharField(max_length=100, null=True, blank=True)
    social_links = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    is_moder = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)

    class Meta:
        ordering = ['user']
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return f"{self.user.username}'s account"

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта ')

    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар',
                               **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Номер телефон',
                             **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна',
                               **NULLABLE)
    tg_chat_id = models.IntegerField(verbose_name='Телеграм id', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

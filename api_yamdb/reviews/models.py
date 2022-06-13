from django.contrib.auth.models import AbstractUser

from django.db import models

ROLES = (
    ('user', 'Пользователь'),
    ('admin', 'Администратор'),
    ('moderator', 'Модератор')
)


class User(AbstractUser):
    email = models.EmailField('Почта', max_length=254, unique=True)
    first_name = models.CharField('Имя', max_length=150, blank=True)
    last_name = models.CharField('Фамилия', max_length=150, blank=True)
    bio = models.TextField('Биография', blank=True, null=True)
    role = models.CharField('Роль', choices=ROLES, default='user')
    confirmation_code = models.CharField(
        'Код подтвержения', max_length=100,
        blank=True
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.username

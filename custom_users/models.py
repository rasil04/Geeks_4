from django.db import models
from django.contrib.auth.models import User

USER_TYPE = (
    ('Admin', 'Admin'),
    ('VIP', "VIP"),
    ('User', 'User')
)

GENDER = (
    ('Male', "Male"),
    ('Female', 'Female')
)

ORIENTATION = (
    ('STRAIGHT', 'STRAIGHT'),
    ('GAY', 'GAY'),
    ('LESBIAN', 'LESBIAN'),
    ('BI', 'BI')
)

MARRY_TYPE = (
    ('MARRIED', 'MARRIED'),
    ('SINGLE', 'SINGLE'),
)

YES = 1
NO = 2
I_DONT_KNOW = 3

LIKE_IT = (
    (YES, 'YES!'),
    (NO, 'NO!'),
    (I_DONT_KNOW, 'I DONT KNOW!'),
)


class CustomUser(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user_type = models.CharField(max_length=100, choices=USER_TYPE, verbose_name='Тип пользователя')
    phone_number = models.CharField(verbose_name='Номер телефона', null=True, max_length=100)
    age = models.PositiveIntegerField('Возраст')
    gender = models.CharField(max_length=100, choices=GENDER)
    birthday = models.CharField('Дата рождения', max_length=30)
    orientation = models.CharField(max_length=100, verbose_name='Ориентация', choices=ORIENTATION)
    marry = models.CharField(max_length=100, verbose_name='Семейное положение', choices=MARRY_TYPE)
    city = models.CharField('Город', max_length=40)
    favorite_film = models.CharField('Любимый фильм', max_length=45)
    it = models.IntegerField(choices=LIKE_IT, verbose_name='Нравится ли вам IT сфера?')
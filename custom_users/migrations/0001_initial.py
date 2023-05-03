# Generated by Django 4.2 on 2023-05-03 17:44

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_type', models.CharField(choices=[('Admin', 'Admin'), ('VIP', 'VIP'), ('User', 'User')], max_length=100, verbose_name='Тип пользователя')),
                ('phone_number', models.CharField(max_length=100, null=True, verbose_name='Номер телефона')),
                ('age', models.PositiveIntegerField(verbose_name='Возраст')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('birthday', models.CharField(max_length=30, verbose_name='Дата рождения')),
                ('orientation', models.CharField(choices=[('STRAIGHT', 'STRAIGHT'), ('GAY', 'GAY'), ('LESBIAN', 'LESBIAN'), ('BI', 'BI')], max_length=100, verbose_name='Ориентация')),
                ('marry', models.CharField(choices=[('MARRIED', 'MARRIED'), ('SINGLE', 'SINGLE')], max_length=100, verbose_name='Семейное положение')),
                ('city', models.CharField(max_length=40, verbose_name='Город')),
                ('favorite_film', models.CharField(max_length=45, verbose_name='Любимый фильм')),
                ('it', models.IntegerField(choices=[(1, 'YES!'), (2, 'NO!'), (3, 'I DONT KNOW!')], verbose_name='Нравится ли вам IT сфера?')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

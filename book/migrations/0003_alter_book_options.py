# Generated by Django 4.2 on 2023-04-26 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_book_update_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книгу', 'verbose_name_plural': 'Книги'},
        ),
    ]
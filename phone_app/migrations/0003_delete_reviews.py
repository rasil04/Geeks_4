# Generated by Django 4.2 on 2023-05-03 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phone_app', '0002_alter_phones_options_alter_phones_video_reviews'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]
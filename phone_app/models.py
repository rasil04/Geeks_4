from django.db import models

class Phones(models.Model):
    MODEL_PHONE = (
        ('Простые', 'Простые'),
        ('Бюджетные', 'Бюджетные'),
        ('Высокого класса', 'Высокого класса'),
        ('Премиум класса', 'Премиум класса'),
        ('Элитные', 'Элитные')
    )
    title = models.CharField("Название телефона", max_length=100)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Фото", upload_to=(''))
    video = models.URLField("Видео", blank=True)
    cost = models.PositiveIntegerField("Цена")
    model_phone = models.CharField("Модель телефона", max_length=100, choices=MODEL_PHONE)
    created_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.title

from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Фамилие')
    last_name = models.CharField(max_length=100, verbose_name='Имя', blank=True)
    phone = models.CharField(max_length=100, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Почта', blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('На обработке', 'На обработке'),
        ('Выехал', 'Выехал'),
        ('Доставлен', 'Доставлен')
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.status
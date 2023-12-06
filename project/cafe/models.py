from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категорія')
    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=255, verbose_name='Інгредіент')
    quantity = models.CharField(max_length=255, verbose_name='Кількість')
    item = models.ForeignKey('Item', on_delete=models.CASCADE, verbose_name='Страва')

    class Meta:
        verbose_name = 'Інгредіент'
        verbose_name_plural = 'Інгредіенти'

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Страва')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    description = models.TextField()
    image = models.ImageField(upload_to='item_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категорія')

    class Meta:
        verbose_name = 'Назва'
        verbose_name_plural = 'Назви'

    def __str__(self):
        return self.name


class Order(models.Model):
    customer_name = models.CharField(max_length=255, verbose_name='Замовник')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефону')
    items = models.ManyToManyField(Item, verbose_name='Ваше замовлення:')

    def __str__(self):
        return f'Order for {self.customer_name}'


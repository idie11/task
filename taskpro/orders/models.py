from users.models import Courier
from django.db import models
from django.db.models.base import Model

class Order(models.Model):

    CHOICES = (
        ('W','Waiting'),
        ('M','Order_is_made'),
        ('R','Rejected')
    )

    customer = models.ForeignKey('users.Customer', models.CASCADE, 'orders')
    courier = models.ForeignKey('users.Courier', models.CASCADE, 'orders')
    order_date = models.DateTimeField('Дата заказа', auto_now_add=True)
    address = models.CharField('Адресс', max_length=255)
    status = models.CharField('Статус', max_length=255, choices = CHOICES)
    total_price = models.DecimalField('Общая сумма')




class OrderProduct(models.Model):
    quantity = models.PositiveIntegerField('Количество', default=1)
    product = models.ForeignKey('products.Product', models.CASCADE, 'orders')
    order = models.ForeignKey(Order, models.CASCADE, 'product')
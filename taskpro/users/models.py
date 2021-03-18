from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    email = models.EmailField()
    avatar = models.ImageField('Аватар', upload_to='user_avatar/', null=True, blank=True)
      


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Courier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    car_number = models.CharField('Номер машины', max_length=25, null=True, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE, related_name='user')
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=255)
    address = models.CharField('Адрес', max_length=255)  
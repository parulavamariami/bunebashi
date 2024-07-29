from django.db import models
from django.contrib.auth.models import AbstractUser

class Username(models.Model):
    fullname = models.CharField(max_length=300)
    contact = models.IntegerField()
    about = models.TextField()

    def __str__(self):
        return self.fullname

class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Service(models.Model):
    picture = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    type = models.ManyToManyField(Type, related_name='services', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    username = models.ForeignKey(Username, on_delete=models.SET('404! USER NOT FOUND!'))
    description = models.TextField()

    def __str__(self):
        return f'{self.title} by {self.username}'

class User(AbstractUser):
    services = models.ManyToManyField(Service, related_name='users', blank=True)
    avatar = models.ImageField(null=True, default='avatar.svg')
    bio = models.TextField(null=True)

from re import M
from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=11)

class post(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    content = models.CharField(max_length=10000)

    def __str__(self):
        return self.title
    
class comment(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='cars')
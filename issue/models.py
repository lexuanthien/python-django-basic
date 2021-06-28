from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=10000, null=True, blank=True)
    type = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
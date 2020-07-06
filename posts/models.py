from django.db import models

# Create your models here.
class Post(models.Model):
    time = models.CharField(null=True, max_length=200)

class Credit(models.Model):
    title = models.CharField(null=True, max_length=100)
    credit = models.CharField(null=True, max_length=200)
    grade = models.CharField(null=True, max_length=200)
    time = models.CharField(null=True, max_length=200)
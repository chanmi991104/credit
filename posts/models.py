from django.db import models

# Create your models here.
class Post(models.Model):
    time = models.CharField(max_length=200)

class Credit(models.Model):
    title = models.CharField(max_length=100)
    credit = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)

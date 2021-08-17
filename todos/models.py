from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank=False)

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TestModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
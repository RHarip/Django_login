from django.db import models

# Create your models here.

class Guest(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

    def __str__(self):
        return str(self.username)
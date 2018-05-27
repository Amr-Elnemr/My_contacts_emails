from django.db import models

# Create your models here.

class Contacts(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        unique=True,
    )
    email = models.EmailField(
        max_length=254,
        blank=False,
        unique=True,
    )
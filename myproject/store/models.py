from django.db import models
from django.db.models import ForeignKey
from django.contrib.auth.hashers import make_password, check_password


# Create your models here.

class Items(models.Model):
    title = models.CharField(max_length=150, blank=False)
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=False)
    cat = models.ForeignKey("Category", on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=120, db_index=True)

    def __str__(self):
        return self.name
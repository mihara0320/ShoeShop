from __future__ import unicode_literals
from django.db import models
from datetime import datetime

CATEGORY_OPTIONS = (
    ('1', 'shoes'),
    ('2', 'boots'),
)

class Item(models.Model):
    name = models.CharField(max_length = 50, default='Empty')
    brand = models.CharField(max_length = 30, default='Empty')
    category = models.CharField(max_length=1, choices=CATEGORY_OPTIONS, default='1')
    image = models.ImageField(upload_to='item_images/')
    description = models.TextField(default='Empty')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('coffee', 'Coffee'),
        ('sandwich','sandwich'),
        ('tea','Tea'),
        ('pastry','Pastry'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank = True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

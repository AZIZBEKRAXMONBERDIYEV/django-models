from django.db import models

quality_choices = (
    ('n', "New"),
    ('o', "Old")
)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField(default=00.00)
    quantity = models.PositiveIntegerField(default=0)
    is_there = models.BooleanField(default=True)
    quality = models.CharField(max_length=20, choices=quality_choices, default='New')

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.FloatField(blank=False)
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

class Category(models.Model):
    category = models.CharField(blank=False, max_length=100)
    
    def __str__(self):
        return self.category

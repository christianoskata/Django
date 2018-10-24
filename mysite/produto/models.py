from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

class Produto(models.Model):

    name = models.CharField(max_length= 50, unique=True)
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    image = models.ImageField(upload_to='produto/images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    tags = TaggableManager()
    views = models.IntegerField(default=0)

    class Meta:

        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['-views']

from django.db import models
from django.utils.text import slugify


class Product(models.Model):
    name= models.CharField(max_length=100)
    slug = models.SlugField(unique=True  , null=True , blank=True)
    category = models.CharField(max_length=100)
    description= models.TextField()
    cut_price= models.IntegerField(default=0)
    price= models.IntegerField(default=0)
    category= models.CharField(max_length=20)
    image = models.ImageField(upload_to='static/upload_images/',blank=False)

    def save(self , *args , **kwargs):
        self.slug = slugify(self.name)
        super(Product ,self).save(*args , **kwargs)


    def __str__(self) -> str:
        return self.name

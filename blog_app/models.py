from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True , null=True , blank=True)


    def save(self , *args , **kwargs):
        self.slug = slugify(self.category_name)
        super(Category ,self).save(*args , **kwargs)


    def __str__(self) -> str:
        return self.category_name


class Post(models.Model):
    title= models.CharField(max_length=300)
    slug = models.SlugField(unique=True  , null=True , blank=True)
    author = models.CharField(max_length=300)
    # body = models. TextField()
    body = RichTextField(blank=True, null=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name="posts", null=True)
    blog_image = models. ImageField(upload_to='static/blog_images/',blank=False)

    def save(self , *args , **kwargs):
        self.slug = slugify(self.title)
        super(Post ,self).save(*args , **kwargs)


    def __str__(self) -> str:
        return self.title

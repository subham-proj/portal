from django.core.files.storage import FileSystemStorage
from django.db import models
fs = FileSystemStorage(location='/media/img')

from ckeditor.fields import RichTextField
from datetime import date
from django.template.defaultfilters import slugify
from .utils import unique_slug_generator
from django.utils import timezone

# Create your models here.

class Query(models.Model):

    email = models.EmailField(max_length=100)
    query = models.TextField(max_length=2000)


class Category(models.Model):
    content = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)
    

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self.content,Category)

        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

class Blogs(models.Model):
    
    question = models.TextField(max_length=2000)

    answer = RichTextField()
    code = RichTextField()

    name = models.CharField(max_length=100,null=True,blank=True)
    college_name = models.CharField(max_length=200,null=True,blank=True)

    facebook = models.CharField(max_length=100,null=True,blank=True) 
    linkedin = models.CharField(max_length=100,null=True,blank=True)
    twitter = models.CharField(max_length=100,null=True,blank=True)
    instagram = models.CharField(max_length=100,null=True,blank=True)

    tags = models.ManyToManyField(Category)

    slug = models.SlugField()

    published_on = models.DateTimeField(null=True,default=timezone.now)

    def __str__(self):
        return self.question

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = unique_slug_generator(self.question,Blogs)

        super(Blogs, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"



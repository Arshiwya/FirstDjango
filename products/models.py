from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth.models import User



class ProductManager(models.Manager):
    def published (self):

        return self.filter(status = 'p')


class CategoryManager(models.Manager):
    def published (self):
        return self.filter(status = True)


class Category(models.Model):
    title = models.CharField(max_length=100 , null=False , blank=False)
    slug = models.SlugField(max_length=50 , unique=True)
    image = models.ImageField(upload_to='categories' ,null=True , blank=True)
    status = models.BooleanField(default=True)
    parent = models.ForeignKey('self' , on_delete=models.CASCADE ,related_name='subcat' ,blank=True, null=True)








    class Meta :
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['status']


    def __str__(self):
        return self.title

    def get_thumbnail(self):
        return format_html(f"<img width='70' style='border-radius: 10px;' src='{self.image.url}'>")
    get_thumbnail.short_description = 'thumbnail'

    objects = CategoryManager()


class Product(models.Model):

    STATUS_CHOICES = (
        ('d' ,'draft'),
        ('p' , 'publish')
    )


    admin = models.ForeignKey(User , null=True , on_delete = models.SET_NULL , related_name='admin')
    title = models.CharField(max_length=50 , null=False , blank=False)
    slug = models.SlugField(max_length=50 , unique=True )
    description =models.TextField()
    categories = models.ManyToManyField('Category' , related_name='product' )
    price = models.BigIntegerField(null=True)
    image = models.ImageField(upload_to='products')
    created = models.DateTimeField(auto_now_add=True)
    #published = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1 , default='p' , choices=STATUS_CHOICES)
    stars = models.SmallIntegerField(default=0)


    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['-created']

    def __str__(self):
        return self.title

    def Rstars(self):
        return range(self.stars)

    def get_thumbnail(self):
        return format_html(f"<img width='70' style='border-radius: 10px;' src='{self.image.url}'>")
    get_thumbnail.short_description = 'thumbnail'








    objects = ProductManager()



# class User (models.Model):
#     name = models.CharField(max_length=50 , null=False , blank= False)
#     lastname = models.CharField(max_length=50 , null=False , blank=False)
#     username = models.CharField(max_length=50 , null=False , blank=False , unique=True)







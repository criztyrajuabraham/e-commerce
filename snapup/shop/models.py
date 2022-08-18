from django.db import models


# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name=models.CharField(max_length=300)
    slug=models.SlugField(max_length=100, unique=True)
    description=models.TextField()
    image=models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('shop:product_list_by_category',args=[self.slug])



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name=models.CharField(max_length=100, unique=True)
    slug=models.SlugField(max_length=100, unique=True)
    desc1=models.TextField()
    price=models.DecimalField(max_digits=7, decimal_places=2)
    img=models.ImageField(upload_to='product', blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('shop:prodCatDetail',args=[self.category.slug,self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name


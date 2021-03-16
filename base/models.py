from django.db import models
from django.urls import reverse
class Destination(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    description = models.CharField(max_length=300, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.CharField(max_length=300, db_index=True)


    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('base:product_list_by_category', args=[self.slug])
class Sategory(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.CharField(max_length=300, db_index=True)


    class Meta:
        ordering = ('name', )
        verbose_name = 'sategory'
        verbose_name_plural = 'sategories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('base:product_list_by_sategory', args=[self.slug])
class Product(models.Model):
    sategory = models.ForeignKey(Sategory, related_name='products', on_delete=models.CASCADE)
    destinations = models.ForeignKey(Destination, related_name='destination', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('base:sub_product_list', args=[self.id, self.slug])  
    def get_absolute_url_price(self):
        return reverse('base:sub_product_list_price', args=[self.price])  
   

# Create your models here.

from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model

User=get_user_model()

class Category(models.Model):
    name=models.CharField(unique=True,max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,unique=True)
    
    def get_absolute_url(self):
        return reverse('auction:items_by_category',args=[self.slug])
    
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    
    def __str__(self):
        return self.name 

class Seller(models.Model):
    name=models.CharField(max_length=200)
    seller_photo=models.ImageField(upload_to='photos/seller/%Y/%m/%d/')
    contact_no =models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    def get_absolute_url(self):
        return reverse('auction:seller-page',args=[self.id])
    
    def __str__(self):
        return self.name
    

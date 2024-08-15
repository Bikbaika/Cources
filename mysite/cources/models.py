from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('cources:course_list_by_category',
                       args=[self.slug])
    


class Course(models.Model):

    category = models.ForeignKey(Category, related_name='cources', on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='courses/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField()

    class Meta:
        ordering =('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('cources:course_detail', args=[self.id, self.slug])
    

# Create your models here.

from django.db import models
from cources.models import Course

class Order(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering=['-created']

    def __str__(self):
        return f'Заказ {self.id}'
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name= 'items', on_delete=models.CASCADE)
    course = models.ForeignKey(Course,related_name= 'order_items', on_delete=models.CASCADE )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price*self.quantity
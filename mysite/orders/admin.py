from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['course']
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email','paid', 'created', 'update']
    list_filter = ['paid', 'created', 'update']
    inlines = [OrderItemInLine]



# Register your models here.

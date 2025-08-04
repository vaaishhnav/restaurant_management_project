from django.db import models

# Create your models here.
# orders/models.py

from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
            ('PENDING', 'Pending'),
            ('CONFIRMED', 'Confirmed'),
            ('PREPARING', 'Preparing'),
            ('DELIVERED', 'Delivered'),
            ('CANCELLED', 'Cancelled'),
        ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_items = models.ManyToManyField(Product, through='OrderItem')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"

    class OrderItem(models.Model):
        order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
        product = models.ForeignKey(Product, on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField(default=1)

        def __str__(self):
            return f"{self.quantity} x {self.product.name} for Order #{self.order.id}"

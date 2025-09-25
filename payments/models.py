from django.db import models
from django.conf import settings
from orders.models import Order

class Payment(models.Model):
    METHOD_CHOICES = [
        ("MPESA", "M-Pesa"),
        ("CARD", "Credit/Debit Card"),
        ("PAYPAL", "PayPal"),
        ("CASH", "Cash on Delivery"),
    ]

    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("SUCCESS", "Success"),
        ("FAILED", "Failed"),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="payment")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id} - {self.order.id} - {self.status}"

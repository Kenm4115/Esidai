from rest_framework import serializers
from .models import Payment
from orders.models import Order

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["id", "order", "user", "amount", "method", "status", "transaction_id", "created_at"]
        read_only_fields = ["user", "status", "transaction_id", "created_at"]

    def create(self, validated_data):
        user = self.context["request"].user
        order = validated_data["order"]

        # Ensure the order belongs to the user
        if order.user != user and not user.is_staff:
            raise serializers.ValidationError("You cannot pay for someone else’s order.")

        # Prevent duplicate payments
        if hasattr(order, "payment"):
            raise serializers.ValidationError("This order already has a payment.")

        payment = Payment.objects.create(
            user=user,
            **validated_data,
            status="SUCCESS",  # For now, assume payment always succeeds
            transaction_id=f"TXN-{order.id}-{user.id}"
        )

        # Mark order as PAID
        order.status = "PAID"
        order.save()

        return payment

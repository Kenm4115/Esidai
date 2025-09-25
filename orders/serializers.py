from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product
from products.serializers import ProductSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = OrderItem
        fields = ["id", "product", "product_id", "quantity", "price"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id", "user", "status", "total_price", "created_at", "updated_at", "items"]
        read_only_fields = ["user", "total_price"]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)

        total = 0
        for item_data in items_data:
            product_id = item_data.get("product_id")
            quantity = item_data.get("quantity")
            price = item_data.get("price")

            # Fetch product
            product = Product.objects.get(id=product_id)

            # Check stock availability
            if product.stock < quantity:
                raise serializers.ValidationError(
                    {"error": f"Not enough stock for {product.name}. Available: {product.stock}"}
                )

            # Reduce stock
            product.stock -= quantity
            product.save()

            # Create order item
            OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)

            total += price * quantity

        order.total_price = total
        order.save()
        return order

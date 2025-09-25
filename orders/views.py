from rest_framework import viewsets, permissions
from .models import Order
from .serializers import OrderSerializer

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission:
    - Users can only view their own orders.
    - Only admins/staff can update status.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True  # Admin can do anything
        return obj.user == request.user  # Customers: only their own orders


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_staff:
            # Admin sees all orders
            return Order.objects.all().order_by("-created_at")
        # Customers only see their own
        return Order.objects.filter(user=self.request.user).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        # Prevent customers from changing status
        if not self.request.user.is_staff:
            serializer.validated_data.pop("status", None)
        serializer.save()

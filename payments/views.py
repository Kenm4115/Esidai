from rest_framework import viewsets, permissions
from .models import Payment
from .serializers import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Payment.objects.all().order_by("-created_at")
        return Payment.objects.filter(user=user).order_by("-created_at")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

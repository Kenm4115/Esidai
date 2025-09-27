from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from .permissions import ReadOnlyOrAuthenticated


class CategoryViewSet(viewsets.ModelViewSet):
    """API endpoint for managing product categories."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        """Allow public access for listing and retrieving, restrict modifications."""
        if self.action in ["list", "retrieve"]:  # Anyone can view categories
            return [AllowAny()]
        return [IsAuthenticated()]  # Only authenticated users can create/update/delete


class ProductViewSet(viewsets.ModelViewSet):
    """API endpoint for managing products."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ReadOnlyOrAuthenticated]

    # Filtering, search, and ordering options for API
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["category", "price"]   # filter by category or price
    search_fields = ["name", "description"]    # search by name or description
    ordering_fields = ["price", "created_at"]  # order by price or date added


def product_list(request):
    """Render product list as an HTML template."""
    products = Product.objects.all()
    return render(request, "products/product_list.html", {"products": products})

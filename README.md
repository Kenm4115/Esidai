### Esidai

# Esidai is an e-commerce platform for selling organic food products.

# This repository contains the backend API built with Django & Django REST Framework (DRF).

## 🚀 Features
    ✅ Core
            •	User authentication & profiles (JWT).
            •	Product catalog with categories (Honey, Eggs, Others).
            •	Shopping cart (add, remove, update items).
            •	Order creation & management.
            •	Payment integration (Stripe / PayPal / M-Pesa).
    ⭐ Enhancements
            •	Product reviews & ratings.
            •	Order tracking (pending, paid, shipped, delivered).
            •	Admin API for product & order management.
            •	Analytics: top-selling products, sales reports.

## System Architecture
    •	Backend: Django + Django REST Framework
    •	Database: PostgreSQL (recommended)
    •	Authentication: JWT (djangorestframework-simplejwt)
    •	Payments: Stripe / PayPal / M-Pesa API
    •	Media: Cloudinary / S3 (for product images)
    •	Deployment: Docker + Gunicorn + Nginx

## API Endpoints
    Accounts
        •	POST /api/accounts/register/ → Register new user
        •	POST /api/accounts/login/ → Login (JWT)
        •	GET /api/accounts/profile/ → User profile
    Products
        •	GET /api/products/ → List all products
        •	GET /api/products/{id}/ → Product details
        •	POST /api/products/ → Add product (Admin only)
    Cart
        •	GET /api/cart/ → View cart
        •	POST /api/cart/add/ → Add item
        •	DELETE /api/cart/remove/{id}/ → Remove item
    Orders
        •	POST /api/orders/create/ → Create order from cart
        •	GET /api/orders/{id}/ → Order details
    Payments
        •	POST /api/payments/checkout/ → Process payment
    # Reviews
        •	POST /api/reviews/{product_id}/ → Add review
        •	GET /api/reviews/{product_id}/ → View reviews

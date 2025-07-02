from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework import permissions

from django.contrib.auth.models import User

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path("admin/", admin.site.urls),
    # ------------------------------------
    path("auth/", include("apps.users.urls")),
    # path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # ------------------------------------
    path("product/", include("apps.products.urls")),
    path("cart/", include("apps.carts.urls")),
    # path("order/", include("apps.orders.urls")),
    # path("payment/", include("apps.payment.urls")),
]

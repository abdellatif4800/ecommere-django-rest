from django.db import models
from django.contrib.auth.models import User


class Order_Item(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    item_total = models.IntegerField(default=0)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    items = models.ManyToManyField(Order_Item)
    order_total = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    shipping_address = models.TextField(null=True)
    order_notes = models.TextField(null=True)

    #  ------------------------------------
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    # *********************
    ORDER_STATUS = {
        PENDING: "pending",
        PROCESSING: "processing",
        SHIPPED: "shipped",
        DELIVERED: "delivered",
    }
    shipping_status = models.CharField(
        choices=ORDER_STATUS,
        default=PENDING,
    )

    #  ------------------------------------
    CASH_ON_DELIVERY = "cash on delivery"
    BY_CARD = " "

    # *********************
    PAYMENT_METHOD = {CASH_ON_DELIVERY: "cash on delivery", BY_CARD: "by card"}
    payment_method = models.CharField(choices=PAYMENT_METHOD, default=CASH_ON_DELIVERY)

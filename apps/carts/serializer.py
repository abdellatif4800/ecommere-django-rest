from .models import Cart, Item
from apps.products.serializer import RetriveProductSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from django.utils import timezone

from apps.carts import models


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"

    product = RetriveProductSerializer()
    quantity = serializers.IntegerField()
    item_total = serializers.IntegerField()

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    items = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), many=True)
    cart_total = serializers.IntegerField(read_only=True)
    updated_at = serializers.DateTimeField(default=None)

    # def create(self, validated_data):
    #     return Cart.objects.create(**validated_data)
    #
    def update(self, instance, validated_data):
        if "cart_total" in validated_data:
            instance.cart_total = validated_data["cart_total"]

        if "items" in validated_data:
            instance.items = validated_data["items"]

        instance.updated_at = timezone.now()
        instance.save()
        return instance

from .models import Product, Image
from rest_framework import serializers
from django.utils import timezone


class ImageSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ["id", "name", "photo_url"]  # photo is an ImageField

    def get_photo_url(self, obj):
        return obj.photo.url if obj.photo else None


class CreateModifyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "descreption",
            "price",
            "stock",
            "category",
            "images",
        ]

    images = ImageSerializer(many=True, read_only=True)

    def create(self, validated_data):
        images = validated_data.pop("images", [])
        product = Product.objects.create(**validated_data)

        for image in images:
            Image.objects.create(product=product, photo=image, name=image.name)
        return product

    def update(self, instance, validated_data):
        if "name" in validated_data:
            instance.name = validated_data["name"]

        if "descreption" in validated_data:
            instance.descreption = validated_data["descreption"]

        if "price" in validated_data:
            instance.price = validated_data["price"]

        if "stock" in validated_data:
            instance.stock = validated_data["stock"]
        instance.updated_at = timezone.now()
        instance.save()
        return instance


class RetriveProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"

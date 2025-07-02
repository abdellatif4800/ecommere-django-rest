# from enum import unique
# from django.db import models
# from django.utils import timezone


# class User(models.Model):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     email = models.EmailField(max_length=254, unique=True)
#     password = models.CharField(max_length=254)
#     joined_at = models.DateTimeField(default=timezone.now)
#     orders = models.ManyToManyField(
#         "orders.Order",
#         related_name="user_orders",
#         blank=True,
#     )

#     @property
#     def username(self):
#         return f"{self.first_name} {self.last_name}"

#     def save(self, *args, **kwargs):
#         print("user registered")
#         super().save(*args, **kwargs)

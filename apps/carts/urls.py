from django.urls import path, include

# from .views import add_item, remove_item
from .views import Cart_view, Item_view, change_quantity
from rest_framework.urlpatterns import format_suffix_patterns


# urlpatterns = [path("addItemToCart/", add_item), path("removeItem/", remove_item)]
urlpatterns = [
    path("addItemToCart/", Item_view.as_view()),
    path("removeItemFormCart/", Item_view.as_view()),
    path("changeQuantity/", change_quantity),
    # --------------------------
    path("getCart/<int:user_id>/", Cart_view.as_view()),
    # --------------------------
]

urlpatterns = format_suffix_patterns(urlpatterns)

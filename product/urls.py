from django.urls import path
from . import views
app_name = "product"
urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("add/", views.add_product, name="add_product"),
]

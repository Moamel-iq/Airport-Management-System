from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from ninja import Router

User = get_user_model()

cart_controller = Router(tags=['Carts'])


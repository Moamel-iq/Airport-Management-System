from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from ninja import NinjaAPI

# from .airport.controllers import airport_controller
from backend.account.controllers import auth_controller

api = NinjaAPI()
api.add_router('/auth', auth_controller)
# api.add_router('/airport', airport_controller)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a/', api.urls)

]

from django.urls import path

from explosive_zone_app import views

urlpatterns = [
    path("", views.index, name="index"),
]

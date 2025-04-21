from django.urls import path

from . import views

urlpatterns = [
    path("stripehook", views.stripe_webhook, name="stripehook"),
]

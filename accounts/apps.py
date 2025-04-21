from django.apps import AppConfig
from django.db.models.signals import post_save

from .signals import send_offer_email


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"

    def ready(self) -> None:
        from .models import Offer

        post_save.connect(send_offer_email, sender=Offer)

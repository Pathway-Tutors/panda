import uuid

from django.db import models

# Create your models here.


class Offer(models.Model):
    id = models.UUIDField(
        "offer_id", primary_key=True, default=uuid.uuid4, editable=False
    )
    frequency = models.CharField("session frequency", max_length=75)
    notes = models.CharField(max_length=250)

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TutorPrice(models.Model):
    tutor = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    price_per_hour = models.PositiveSmallIntegerField(blank=False, null=False)

    def __str__(self):
        return "Price for {}".format(str(self.tutor))

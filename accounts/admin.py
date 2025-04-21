from django.contrib import admin

# Register your models here.
from .models import Offer, Application, DecisionReason

admin.site.register((Offer, Application, DecisionReason))

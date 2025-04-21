from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def stripe_webhook(request):
    return HttpResponse("Hey from stripe webhook")

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from django.shortcuts import render
from django.contrib.auth.models import User

from .forms import UserCreateForm
from .models import Application

if TYPE_CHECKING:
    from django.http import HttpRequest

# Create your views here.


def create_user(request: HttpRequest):
    if request.method and request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            user_id = uuid.uuid4()
            username = "{}_{}_{}".format(
                data["first_name"].lower(), data["last_name"].lower(), user_id.hex
            )
            user = User.objects.create_user(
                username=username,
                email=data["email"],
                first_name=data["first_name"],
                last_name=data["last_name"],
            )

            application = Application(
                student=user, subjects=data["subjects"], notes=data["notes"]
            )
            application.save()

        return render(request, "accounts/thanks.html", context={"email": data["email"]})

    form = UserCreateForm()
    return render(request, "accounts/create_user.html", context={"form": form})

from django.db import models
from django.contrib.auth.models import User

from finance.models import TutorPrice

# Create your models here.


class Application(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    class ApplicationStatus(models.TextChoices):
        PENDING = "pending"
        SUCCESSFUL = "successful"
        REJECTED = "unsuccessful"

    status = models.CharField(
        max_length=12,
        choices=ApplicationStatus,
        default=ApplicationStatus.PENDING,
        null=False,
        blank=False,
    )
    subjects = models.TextField(max_length=300, blank=False, null=False)
    notes = models.TextField(max_length=500, blank=True, null=False)

    def __str__(self):
        return "{} [{}] [{}]".format(
            self.student.get_full_name(),
            self.status.title(),
            self.student.get_username(),
        )


class DecisionReason(models.Model):
    application = models.OneToOneField(
        Application, on_delete=models.CASCADE, primary_key=True
    )
    reason = models.TextField(max_length=1785)
    diagnostic_results = models.TextField(max_length=500)

    def __str__(self):
        return "Decision Reason for {}".format(str(self.application))


class Offer(models.Model):
    student = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="student"
    )
    tutor = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="tutor"
    )
    frequency = models.CharField("session frequency", max_length=75, editable=True)
    reason = models.TextField(
        "frequency reason", max_length=250, blank=False, null=False
    )
    notes = models.TextField("offer notes", max_length=300, blank=True, null=False)
    price = models.ForeignKey(
        TutorPrice, on_delete=models.SET_NULL, unique=False, null=True
    )
    offer_email_sent = models.BooleanField(default=False, editable=True, null=False)

    def __str__(self):
        return "{} [{}]".format(
            self.student.get_full_name(), self.student.get_username()
        )

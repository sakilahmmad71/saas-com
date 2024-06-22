from django.db import models
from django.contrib.auth.models import Group, Permission


# Create your models here.
class Subscription(models.Model):
    name = models.CharField(max_length=100)
    groups = models.ManyToManyField(Group)
    permissions = models.ManyToManyField(
        Permission, limit_choices_to={"content_type__app_label": "subscriptions"}
    )

    class Meta:
        permissions = [
            ("basic", "Basic Permission"),
            ("pro", "Pro Permission"),
            ("advance", "Advance Permission"),
        ]

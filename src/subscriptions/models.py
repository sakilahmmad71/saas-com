from django.db import models
from django.contrib.auth.models import Group, Permission

from django.conf import settings
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL


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

    def __str__(self) -> str:
        return f"{self.name}"


class UserSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(
        Subscription, on_delete=models.SET_NULL, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user} - {self.subscription}"


def user_subscription_post_save(sender, instance, created, **kwargs):
    user_subscription_instance = instance
    user = user_subscription_instance.user

    subscription_object = user_subscription_instance.subscription
    if subscription_object:
        groups = subscription_object.groups.all()
        user.groups.set(groups)


post_save.connect(user_subscription_post_save, sender=UserSubscription)

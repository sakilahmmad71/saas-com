from typing import Any
from django.core.management.base import BaseCommand

from django.conf import settings
from subscriptions.models import Subscription


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> None:
        print("Syncing subscriptions...")
        qs = Subscription.objects.all()

        for subscription in qs:
            subscription_permissions = subscription.permissions.all()
            for group in subscription.groups.all():
                group.permissions.set(subscription_permissions)

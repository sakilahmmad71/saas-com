from typing import Any
from django.core.management.base import BaseCommand

from helpers import download_to_local

VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
}


class Command(BaseCommand):
    help = "Pull the latest version of the vendor repository"

    def handle(self, *args: Any, **options: Any):
        print("Pulling the latest version of the vendor repository")
        for filename, url in VENDOR_STATICFILES.items():
            download_to_local(url, f"vendor/{filename}")
            print(f"Downloaded {filename} from {url}")

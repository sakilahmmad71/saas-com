from typing import Any
from django.core.management.base import BaseCommand

from django.conf import settings
from helpers import download_to_local

STATICFILES_VENDOR_DIR = getattr(settings, "STATICFILES_VENDOR_DIR")

VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
}


class Command(BaseCommand):
    help = "Pull the latest version of the vendor repository"

    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Pulling the latest version of the vendor repository")
        completed_urls = []

        # Download each vendor file
        for filename, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / filename
            download_success = download_to_local(url, out_path)

            if download_success:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Downloaded {filename} from {url} and saved to {out_path}"
                    )
                )
                completed_urls.append(url)
            else:
                self.stdout.write(
                    self.style.ERROR(f"Failed to download {filename} from {url}")
                )

        # Check if all vendor files were downloaded successfully
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS("All vendor files downloaded successfully")
            )
        else:
            self.stdout.write(self.style.ERROR("Failed to download all vendor files"))

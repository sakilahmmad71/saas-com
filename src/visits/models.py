from django.db import models


class Visit(models.Model):
    path = models.TextField(
        help_text="The path visited by the user",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

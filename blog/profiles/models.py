from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profiles"
    )
    age = models.IntegerField()
    image = models.ImageField(blank=True, null=True)
    status = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )
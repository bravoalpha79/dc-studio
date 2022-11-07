from django.db import models

class Cooperation(models.Model):
    content = models.TextField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Pravne osobe"
        verbose_name_plural = "Pravne osobe"


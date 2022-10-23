from django.db import models

class About(models.Model):
    content = models.TextField(null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "O kliničkom studiju"
        verbose_name_plural = "O kliničkom studiju"



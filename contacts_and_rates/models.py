from django.db import models


class ContactInfo(models.Model):
    content = models.TextField(null=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Kontakti i informacije"
        verbose_name_plural = "Kontakti i informacije"

class RateList(models.Model):
    ratelist_pdf = models.FileField(null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Cjenik"
        verbose_name_plural = "Cjenici"

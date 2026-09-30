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
        verbose_name_plural = "Cjenik"


class RateLink(models.Model):
    ratelink_url = models.URLField()
    created_at = models.DateField(auto_now_add=True)
    last_updated_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        return cls.objects.filter(pk=1).first()

    def __str__(self):
        return "Link na sidreni cjenik"

    class Meta:
        verbose_name = "Sidreni cjenik"
        verbose_name_plural = "Sidreni cjenik"

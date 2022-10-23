from django.db import models


class Link(models.Model):
    title = models.CharField(max_length=254, null=True, blank=True)
    url = models.URLField(null=False)
    display = models.BooleanField(null=False, default=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Linkovi"

class StudentLink(models.Model):
    title = models.CharField(max_length=254, null=True, blank=True)
    url = models.URLField(null=False)
    display = models.BooleanField(null=False, default=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Link za studente"
        verbose_name_plural = "Linkovi za studente"

class MediaLink(models.Model):
    title = models.CharField(max_length=254, null=True, blank=True)
    summary = models.TextField(null=False)
    url = models.URLField(null=False)
    display = models.BooleanField(null=False, default=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Ize medija"
        verbose_name_plural = "Iz medija"
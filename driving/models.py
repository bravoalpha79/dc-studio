from django.db import models


class DrivingIndividual(models.Model):
    content = models.TextField(null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Individualni pristup"
        verbose_name_plural = "Individualni pristup"
        

class DrivingGroup(models.Model):
    content = models.TextField(null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Grupni pristup"
        verbose_name_plural = "Grupni pristup"

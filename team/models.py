from django.db import models

# Create your models here.
class TeamMember(models.Model):
    name_and_title = models.CharField(max_length=254, null=False, blank=False)
    biography = models.TextField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = "Član tima"
        verbose_name_plural = "Članovi tima"
        

class Associate(models.Model):
    name_and_title = models.CharField(max_length=254, null=False, blank=False)
    biography = models.TextField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = "Suradnik"
        verbose_name_plural = "Suradnici"
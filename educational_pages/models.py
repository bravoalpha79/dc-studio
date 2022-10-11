from tabnanny import verbose
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=254, null=False, blank=False)
    slug = models.SlugField(null=False, blank=False, default="")
    author = models.CharField(max_length=254, null=True, blank=True)
    tags = models.CharField(max_length=254, null=True, blank=True)
    content = models.TextField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    date_published = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Članak"
        verbose_name_plural = "Članci"

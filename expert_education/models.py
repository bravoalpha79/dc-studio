from django.db import models


class ExpertEducationQuerySet(models.QuerySet):
    def visible(self):
        return self.filter(is_published=True)


class ExpertEducation(models.Model):
    title = models.CharField(max_length=254, null=False, blank=False)
    slug = models.SlugField(null=False, blank=False, default="")
    content = models.TextField(null=False, blank=False)
    is_published = models.BooleanField(null=False, default=False)

    position = models.IntegerField(null=False, default=1)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    objects = ExpertEducationQuerySet.as_manager()

    class Meta:
        verbose_name = "Edukacija stručnjaka"
        verbose_name_plural = "Edukacije stručnjaka"

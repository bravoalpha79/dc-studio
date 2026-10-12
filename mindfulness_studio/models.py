from django.db import models


# add queryset method so that nav link will be visible only if
# the content is marked as published
class MindfulnessStudioQuerySet(models.QuerySet):
    def visible(self):
        return self.filter(is_published=True)


class MindfulnessStudio(models.Model):
    content = models.TextField(null=False, blank=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(null=False, default=False)

    objects = MindfulnessStudioQuerySet.as_manager()

    # allow only one instance of the M.S. model
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        return cls.objects.filter(pk=1).first()

    def __str__(self):
        return "Mindfulness studio"

    class Meta:
        verbose_name = "Mindfulness studio"
        verbose_name_plural = "Mindfulness studio"

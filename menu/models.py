from django.db import models
from django.urls import reverse

from .constants import MAX_NAME_LEGTH, MAX_SLUG_LENGTH, MAX_URL_LENGTH


class MenuItem(models.Model):
    title = models.CharField(max_length=MAX_NAME_LEGTH)
    name = models.CharField(max_length=MAX_NAME_LEGTH)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='children'
    )
    url = models.CharField(max_length=MAX_URL_LENGTH, blank=True)
    slug = models.SlugField(max_length=MAX_SLUG_LENGTH, unique=True)

    def save(self, *args, **kwargs):
        if self.parent:
            self.slug = f'{self.parent.slug.strip("/")}/{self.slug.strip("/")}'
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('catalog_category', args=[self.slug])

    def __str__(self):
        return self.title

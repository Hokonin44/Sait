from django.db import models


class News(models.Model):
    class Meta:
        ordering = ['title']
        verbose_name_plural = 'NEWS'

    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

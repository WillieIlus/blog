from django.db import models
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=254)
    content = models.TextField()
    created = models.TimeField(auto_now=False, auto_now_add=True)
    update = models.TimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"pk": self.pk})

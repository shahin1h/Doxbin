from django.db import models
from django.utils.crypto import get_random_string


# Create your models here.
class doxbin(models.Model):
    title = models.CharField(max_length=20, null=False)
    slug = models.SlugField(default=lambda: get_random_string(length=15), unique=True, null=False)
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.title

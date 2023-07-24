from django.db import models
from django.contrib.auth.models import User

LANGS = (
    ("py", "python"), ("js", "javaScript"), ("cpp", "c++")
)


class Language(models.Model):
    full_name = models.CharField(max_length=32)
    short_name = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.short_name}"


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.ForeignKey(to=Language, on_delete=models.PROTECT, null=True, blank=True)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, related_name='snippets')
    private = models.BooleanField(default=True)

    def __str__(self):
        return f"Snippets {self.name} | {self.user}"
        # return f"Snippets {self.Snippet} | {self.user}"


class Comment(models.Model):
    text = models.TextField(max_length=2500)
    creation_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    snippet = models.ForeignKey(to=Snippet, on_delete=models.CASCADE, related_name='comments')

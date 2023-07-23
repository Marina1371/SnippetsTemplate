from django.contrib import admin
from django.contrib import admin
from MainApp.models import Snippet, Comment, Language

admin.site.register(Snippet)
admin.site.register(Language)
admin.site.register(Comment)
# Register your models here.

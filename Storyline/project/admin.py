from django.contrib import admin
from .models import story, chapter, comments

# Register your models here.
admin.site.register(story)
admin.site.register(chapter)
admin.site.register(comments)

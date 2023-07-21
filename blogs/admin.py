from django.contrib import admin

# Register your models here.

from .models import Topic, Article, User, Comment

admin.site.register(Topic)
admin.site.register(Article)
admin.site.register(User)
admin.site.register(Comment)

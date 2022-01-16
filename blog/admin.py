from django.contrib import admin
from .models import article, Comment, InstagramFeeds
# Register your models here.

admin.site.register(article)
admin.site.register(Comment)
admin.site.register(InstagramFeeds)

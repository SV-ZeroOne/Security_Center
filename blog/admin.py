from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget
from blog.models import Post
from martor.models import MartorField


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']
    formfield_overrides = {
        MartorField: {'widget': AdminMartorWidget},
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Post, PostAdmin)

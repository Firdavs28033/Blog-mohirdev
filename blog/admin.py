from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published')
    list_filter = ('is_published', 'created_at')
    actions = ['publish_posts']

    def publish_posts(self, request, queryset):
        queryset.update(is_published=True)
    publish_posts.short_description = "Selected posts will be published"

admin.site.register(Comment)

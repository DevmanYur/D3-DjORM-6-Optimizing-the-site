from django.contrib import admin
from blog.models import Post, Tag, Comment

class TagsInline(admin.TabularInline):
    model = Post.tags.through
    raw_id_fields = ('post','tag',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['id', 'title', 'published_at', 'author']
    raw_id_fields = ('likes','tags',)
    list_filter = ['published_at', 'tags']

    inlines = [TagsInline,]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

    inlines = [TagsInline, ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('post', 'author',)
    list_display = ['id', 'author', 'published_at']
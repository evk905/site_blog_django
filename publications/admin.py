from django.contrib import admin, messages

from publications.models import Category, Post, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ("category", "author")
    search_fields = ('name', 'text')
    list_display = ('name', 'category', 'author', 'date', 'is_published', 'brief_info')
    list_display_links = ('name', )
    ordering = ['-date', 'name']
    list_editable = ('is_published', 'category')
    list_per_page = 10
    actions = ['set_published', 'set_draft']

    @admin.display(description="Краткое описание", ordering='text')
    def brief_info(self, post: Post):
        return f"В статье {len(post.text)} символов."

    @admin.action(description="Опубликовать")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Post.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей.")

    @admin.action(description="Снять с публикации")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Post.Status.DRAFT)
        self.message_user(request, f"{count} записей сняты с публикации!", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

# admin.site.register(Category)
# admin.site.register(Post, PostAdmin)
# admin.site.register(Tag)
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    list_per_page = 10
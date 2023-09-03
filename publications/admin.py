from django.contrib import admin

from publications.models import Category, Post, Tag, TagsToPosts



class TagInline(admin.TabularInline):
    model = TagsToPosts
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter = ("category", "author")
    search_fields = ('name', 'text')
    list_display = ('id', 'name', 'category', 'author')
    inlines = (TagInline, )


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
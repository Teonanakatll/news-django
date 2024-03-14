from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, About, Post, PostPhoto

from metatags.admin import MetaTagInline

# для изменения виджетов TextField, CharField
from django.forms import TextInput, Textarea
from django.db import models


formfield_overrides = {
    models.CharField: {'widget': TextInput(attrs={'size': '200'})},
    models.TextField: {'widget': Textarea(attrs={'rows': 40, 'cols': 200})},
}


class PostPhotoInline(admin.TabularInline):
    """Вывод фото к статье"""
    model = PostPhoto
    extra = 1
    readonly_fields = ("get_photo",)

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' height=100>")

    get_photo.short_description = "Фото статьи"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Категории"""
    list_display = ("id", "name", "draft", "slug", "description", "get_image", "image")
    list_display_links = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("draft",)
    readonly_fields = ("get_image",)

    formfield_overrides = formfield_overrides

    # инлайн классы, работают со связями ManyToMany и ForeignKey
    inlines = [MetaTagInline]

    def get_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' height=150")

    get_image.short_description = "Фото категории"


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """О сайте"""
    list_display = ("header",)
    list_display_links = ("header",)

    formfield_overrides = formfield_overrides

    # инлайн классы, работают со связями ManyToMany и ForeignKey
    inlines = [MetaTagInline]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Статья"""
    list_display = ("id", "category", "time_create", "get_image", "draft", "short")
    list_display_links = ("category", "time_create", "short")
    list_editable = ("draft",)
    prepopulated_fields = {"slug": ("short",)}
    readonly_fields = ("get_image",)

    formfield_overrides = formfield_overrides

    # инлайн классы, работают со связями ManyToMany и ForeignKey
    inlines = [MetaTagInline, PostPhotoInline]

    def get_image(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' height=100")

    get_image.short_description = "Главное фото"


@admin.register(PostPhoto)
class PostPhotoAdmin(admin.ModelAdmin):
    """Фото статьи"""
    list_display = ("id", "post", "date", "get_photo")
    list_display_links = ("post", "date")
    search_fields = ("post", "date")
    readonly_fields = ("get_photo",)

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' height=100>")

    get_photo.short_description = "Фото статьи"
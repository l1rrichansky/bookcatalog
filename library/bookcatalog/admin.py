from django.contrib import admin
from .models import *


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}


@admin.register(Comment)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("name",)}


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ("title",)}


admin.site.register(File)


@admin.register(Book)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'year', 'series']
    filter_horizontal = ['tags', 'files', 'genres']
    search_fields = ['title', 'series__title']

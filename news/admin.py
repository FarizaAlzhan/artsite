from django.contrib import admin

from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

class ComentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'content','time_create', 'is_published')
    search_fields = ( 'id','content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


class KinoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'rating', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

class MusicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Coments,ComentsAdmin)
admin.site.register(Kino,KinoAdmin)
admin.site.register(Music,MusicAdmin)
admin.site.register(Actor,ActorAdmin)
admin.site.register(News,NewsAdmin)


admin.site.site_title = 'Админ панель сайта Art.kz'
admin.site.site_header = 'Админ панель сайта Art.kz'



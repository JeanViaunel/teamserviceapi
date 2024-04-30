from django.contrib import admin
from .models import Image, Tag, Album

# Register your models here.

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
      list_display = ['title', 'description','cover_image']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
      list_display = ['title', 'description', 'image']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
      pass
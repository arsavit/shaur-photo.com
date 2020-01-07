from django.contrib import admin

from .models import Album, Foto

# Register your models here.

# class FotoAdmin(admin.ModelAdmin):
#     pass


class FotoInline(admin.StackedInline):
    model = Foto
    max_num = 500
    extra = 20


class AlbumAdmin(admin.ModelAdmin):
    inlines = [FotoInline, ]


# admin.site.register(Foto, FotoAdmin)
admin.site.register(Album, AlbumAdmin)
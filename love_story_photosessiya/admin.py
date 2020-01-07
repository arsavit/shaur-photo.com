from django.contrib import admin

from .models import Album_love, Foto_love


# Register your models here.

# class Foto_loveAdmin(admin.ModelAdmin):
#     pass


class Foto_loveInline(admin.StackedInline):
    model = Foto_love
    max_num = 1000
    extra = 20


class Album_loveAdmin(admin.ModelAdmin):
    inlines = [Foto_loveInline, ]


# admin.site.register(Foto_love, Foto_loveAdmin)
admin.site.register(Album_love, Album_loveAdmin)

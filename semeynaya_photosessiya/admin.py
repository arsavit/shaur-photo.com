from django.contrib import admin

from .models import Album_sem, Foto_sem

# Register your models here.

# class Foto_semAdmin(admin.ModelAdmin):
#     pass


class Foto_semInline(admin.StackedInline):
    model = Foto_sem
    max_num = 500
    extra = 20


class Album_semAdmin(admin.ModelAdmin):
    inlines = [Foto_semInline, ]


# admin.site.register(Foto_sem, Foto_semAdmin)
admin.site.register(Album_sem, Album_semAdmin)
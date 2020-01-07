from django.contrib import admin

from .models import Album_nov, Foto_nov

# Register your models here.

# class Foto_novAdmin(admin.ModelAdmin):
#     pass


class Foto_novInline(admin.StackedInline):
    model = Foto_nov
    max_num = 500
    extra = 20


class Album_novAdmin(admin.ModelAdmin):
    inlines = [Foto_novInline, ]


# admin.site.register(Foto_nov, Foto_novAdmin)
admin.site.register(Album_nov, Album_novAdmin)
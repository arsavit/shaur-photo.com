from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Album_nov, Foto_nov

# Register your models here.

# class Foto_novAdmin(admin.ModelAdmin):
#     pass


class Foto_novInline(admin.StackedInline):
    model = Foto_nov
    max_num = 500
    extra = 20
    readonly_fields = ('get_image',)
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="60" height="50"')

    get_image.short_description = 'Изображение'


class Album_novAdmin(admin.ModelAdmin):
    inlines = [Foto_novInline, ]
    date_hierarchy = 'publish'
    prepopulated_fields = {'url': ('title',)}
    list_display = ("title", "get_image",)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.album_poster.url} width="60" height="50"')

    get_image.short_description = 'Изображение'


# admin.site.register(Foto_nov, Foto_novAdmin)
admin.site.register(Album_nov, Album_novAdmin)

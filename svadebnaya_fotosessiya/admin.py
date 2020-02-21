from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Album, Foto

# Register your models here.

# class FotoAdmin(admin.ModelAdmin):
#     pass


class FotoInline(admin.StackedInline):
    model = Foto
    max_num = 500
    extra = 5
    readonly_fields = ('get_image',)
    fieldsets = (
        (None,
         {'fields': (('image', 'width', 'get_image'),)}),
        (None,
         {'fields': (('image_full'),)}),

    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="60" height="50"')

    get_image.short_description = 'Изображение'


class AlbumAdmin(admin.ModelAdmin):
    inlines = [FotoInline, ]
    date_hierarchy = 'publish'
    prepopulated_fields = {'url': ('title',)}
    list_display = ("title", "get_image",)
    readonly_fields = ('get_image',)
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.album_poster.url} width="60" height="50"')

    get_image.short_description = 'Изображение'


# admin.site.register(Foto, FotoAdmin)
admin.site.register(Album, AlbumAdmin)

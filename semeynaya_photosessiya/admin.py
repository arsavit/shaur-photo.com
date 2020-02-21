from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Album_sem, Foto_sem

# Register your models here.

# class Foto_semAdmin(admin.ModelAdmin):
#     pass


class Foto_semInline(admin.StackedInline):
    model = Foto_sem
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


class Album_semAdmin(admin.ModelAdmin):
    inlines = [Foto_semInline, ]
    date_hierarchy = 'publish'
    prepopulated_fields = {'url': ('title',)}
    list_display = ("title", "get_image",)
    readonly_fields = ('get_image',)
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.album_poster.url} width="60" height="50"')

    get_image.short_description = 'Изображение'


# admin.site.register(Foto_sem, Foto_semAdmin)
admin.site.register(Album_sem, Album_semAdmin)

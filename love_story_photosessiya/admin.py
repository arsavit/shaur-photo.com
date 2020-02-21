from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Album_love, Foto_love


# Register your models here.

# class Foto_loveAdmin(admin.ModelAdmin):
#     pass


class Foto_loveInline(admin.StackedInline):
    model = Foto_love
    max_num = 1000
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


class Album_loveAdmin(admin.ModelAdmin):
    inlines = [Foto_loveInline, ]
    date_hierarchy = 'publish'
    prepopulated_fields = {'url': ('title',)}
    list_display = ("title", "get_image",)
    readonly_fields = ('get_image',)
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.album_poster.url} width="60" height="50"')

    get_image.short_description = 'Изображение'


# admin.site.register(Foto_love, Foto_loveAdmin)
admin.site.register(Album_love, Album_loveAdmin)

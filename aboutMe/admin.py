from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import About, Desc
# Register your models here.

class DescInline(admin.StackedInline):
    model = Desc
    max_num = 100
    extra = 1



class AboutAdmin(admin.ModelAdmin):
    inlines = [DescInline, ]
    # list_display = ('get_image',)
    readonly_fields = ('get_image',)
    save_on_top = True
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.avatar.url} width="60" height="50"')

    get_image.short_description = 'Изображение'


admin.site.register(About, AboutAdmin)

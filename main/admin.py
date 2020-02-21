from django.contrib import admin

from .models import Slider_down, Slider_head, Headers

# Register your models here.

class Slider_headInline(admin.StackedInline):
    model = Slider_head
    max_num = 100
    extra = 3


class Slider_downInline(admin.StackedInline):
    model = Slider_down
    max_num = 100
    extra = 5


class HeadersAdmin(admin.ModelAdmin):
    inlines = [Slider_headInline, Slider_downInline ]
    save_on_top = True

# admin.site.register(Slider_head)
# admin.site.register(Slider_down)
admin.site.register(Headers, HeadersAdmin)


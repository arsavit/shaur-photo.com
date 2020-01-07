from django.contrib import admin

from .models import About, Desc, Desc_second
# Register your models here.

class DescInline(admin.StackedInline):
    model = Desc
    max_num = 100
    extra = 1


class Desc_secondInline(admin.StackedInline):
    model = Desc_second
    max_num = 100
    extra = 1


class AboutAdmin(admin.ModelAdmin):
    inlines = [DescInline, Desc_secondInline, ]


admin.site.register(About, AboutAdmin)
# admin.site.register(Desc)
# admin.site.register(Desc_second)
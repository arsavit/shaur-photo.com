from django.contrib import admin

from .models import Album_birt, Foto_birt
from .models import *


# Register your models here.
# class Foto_birtAdmin(admin.ModelAdmin):
#     pass


class Foto_birtInline(admin.StackedInline):
    model = Foto_birt
    max_num = 500
    extra = 20


class Album_birtAdmin(admin.ModelAdmin):
    inlines = [Foto_birtInline, ]


# admin.site.register(Foto_birt, Foto_birtAdmin)
admin.site.register(Album_birt, Album_birtAdmin)

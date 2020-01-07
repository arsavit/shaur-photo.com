from django.contrib import admin

from .models import Album_det, Foto_det

# Register your models here.
# class Foto_detAdmin(admin.ModelAdmin):
#     pass


class Foto_detInline(admin.StackedInline):
    model = Foto_det
    max_num = 500
    extra = 20


class Album_detAdmin(admin.ModelAdmin):
    inlines = [Foto_detInline, ]


# admin.site.register(Foto_det, Foto_detAdmin)
admin.site.register(Album_det, Album_detAdmin)




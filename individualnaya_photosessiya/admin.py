from django.contrib import admin

from .models import Album_ind, Foto_ind

# Register your models here.
# class Foto_indAdmin(admin.ModelAdmin):
#     pass


class Foto_indInline(admin.StackedInline):
    model = Foto_ind
    max_num = 500
    extra = 20


class Album_indAdmin(admin.ModelAdmin):
    inlines = [Foto_indInline, ]


# admin.site.register(Foto_ind, Foto_indAdmin)
admin.site.register(Album_ind, Album_indAdmin)


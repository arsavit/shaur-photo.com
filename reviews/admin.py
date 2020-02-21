from django.contrib import admin

from .models import Autor, Body, Foto

# Register your models here.

class BodyInline(admin.StackedInline):
    model = Body
    max_num = 20
    extra = 1


class AutorAdmin(admin.ModelAdmin):
    inlines = [BodyInline, ]
    save_on_top = True


admin.site.register(Autor, AutorAdmin)
# admin.site.register(Body)
# admin.site.register(Foto)
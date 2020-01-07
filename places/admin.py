from django.contrib import admin

from .models import Places, Sity

# Register your models here.

class PlacesInline(admin.StackedInline):
    model = Places
    max_num = 500
    extra = 3


class SityAdmin(admin.ModelAdmin):
    inlines = [PlacesInline, ]

admin.site.register(Sity, SityAdmin)
# admin.site.register(Places)
from django.contrib import admin

from .models import Price, Price_Description, Tariffs

# Register your models here.

class Price_DescriptionInline(admin.StackedInline):
    model = Price_Description
    max_num = 100
    extra = 1


class TariffsInline(admin.StackedInline):
    model = Tariffs
    max_num = 100
    extra = 1


class PriceAdmin(admin.ModelAdmin):
    inlines = [Price_DescriptionInline, TariffsInline, ]

admin.site.register(Price, PriceAdmin)
# admin.site.register(Price_Description)
# admin.site.register(Tariffs)
from django.contrib import admin
#from django import forms
from .models import Price, Price_Description, Tariffs
#from ckeditor.widgets import CKEditorWidget


#class TariffsAdminForm(forms.ModelForm):
#    tariffs_description = forms.CharField(widget=CKEditorWidget())
#    class Meta:
#        model = Tariffs
#        fields = '__all__'


class Price_DescriptionInline(admin.StackedInline):
    model = Price_Description
    max_num = 100
    extra = 1


class TariffsInline(admin.StackedInline):
    model = Tariffs
    max_num = 100
    extra = 1
#    form = TariffsAdminForm

class PriceAdmin(admin.ModelAdmin):
    inlines = [Price_DescriptionInline, TariffsInline, ]

admin.site.register(Price, PriceAdmin)
# admin.site.register(Price_Description)
# admin.site.register(Tariffs)

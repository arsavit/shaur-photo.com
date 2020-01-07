from django.contrib import admin

from .models import Fotoset, FotosetAdmin

# Register your models here.

admin.site.register(Fotoset, FotosetAdmin)

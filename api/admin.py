from django.contrib import admin
from .models import Receta, RecetaFavorita, Paso

class PasoInline(admin.TabularInline):  # Puedes usar StackedInline en lugar de TabularInline si prefieres ese estilo
    model = Paso
    extra = 1  # Número de conjuntos de campos de Paso que se mostrarán por defecto

class RecetaAdmin(admin.ModelAdmin):
    inlines = [PasoInline]

admin.site.register(Receta, RecetaAdmin)
admin.site.register(RecetaFavorita)
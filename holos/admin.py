from django.contrib import admin
from .models import Generacion

@admin.register(Generacion)
class GeneracionAdmin(admin.ModelAdmin):
    list_display= ('id','nombre', 'tot_integrante_asociados')
    search_fields=('nombre',)
    
    @admin.display(description="Total integrantes asociados")
    def tot_integrante_asociados(self, obj):
        return obj.holomiembros.count()

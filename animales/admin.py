from django.contrib import admin
from .models import Especie, Animal


# Register your models here.
@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('id', 'especie', 'total_animales')
    search_fields = ('especie',)

    @admin.display(description="Total de animales de esta especie")
    def total_animales(self, obj):
        return obj.animales.count()

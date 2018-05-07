from django.contrib import admin
from .models import Cartolas, Rodadas


class CartolasAdmin(admin.ModelAdmin):

	list_display = ['id', 'cartolaNome', 'cartolaTime', 'cartolaImagem']
	search_fields = ['cartolaNome', 'cartolaTime']

class RodadasAdmin(admin.ModelAdmin):

	list_display = ['rodadaId', 'rodadaNome', 'rodadaRealizada']
	search_fields = ['rodadaId', 'rodadaNome']

admin.site.register(Cartolas, CartolasAdmin)
admin.site.register(Rodadas, RodadasAdmin)


# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Inventario
from .models import Tag
from .models import Caixa
from .models import Emprestimo


class InventarioAdmin(admin.ModelAdmin):
	list_display = ('codigo','quantidade','item', 'marca', 'modelo', 'descricao', 'caixa',)
	search_fields = ('codigo','quantidade','item', 'marca', 'modelo', 'descricao', 'caixa',)
	list_filter = ('marca', 'modelo','caixa','tags',)

admin.site.register(Inventario, InventarioAdmin)
admin.site.register(Tag)

class CaixaAdmin(admin.ModelAdmin):
	list_display = ('numero','localizacao','sublocalizacao',)
	search_fields = ('numero','localizacao','sublocalizacao',)
	list_filter = ('localizacao','sublocalizacao',)

admin.site.register(Caixa, CaixaAdmin)


class EmprestimoAdmin(admin.ModelAdmin):
	list_display = ('responsavel','itens','quantidade','status', 'data_saida', 'data_entrada',)
	search_fields = ('responsavel',)
	list_filter = ('responsavel','status','data_saida', 'data_entrada',)

	def itens(self, obj):
		return "\n".join([p.item for p in obj.item.all()])
		

admin.site.register(Emprestimo, EmprestimoAdmin)
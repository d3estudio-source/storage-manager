# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Caixa
from .models import Emprestimo
from .models import Inventario
from .models import Tag
from django.contrib import admin


class InventarioAdmin(admin.ModelAdmin):
	list_display = ('codigo','quantidade','item', 'marca', 'modelo', 'descricao', 'caixa','emprestado_para',)
	search_fields = ('codigo','quantidade','item', 'marca', 'modelo', 'descricao', 'caixa',)
	list_filter = ('marca', 'modelo','caixa','tags',)

	def emprestado_para(self, obj):
		emprestimos = Emprestimo.objects.filter(item__pk=obj.pk)
		return ', '.join([e.responsavel.first_name for e in emprestimos])

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

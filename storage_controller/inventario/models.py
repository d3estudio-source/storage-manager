# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tag(models.Model):
	nome = models.CharField(max_length=10)
	def __unicode__(self):
		return self.nome

class Caixa(models.Model):
	numero = models.IntegerField()
	localizacao = models.CharField(max_length=100)
	sublocalizacao = models.CharField(max_length=100, null=True, blank=True)

	def __unicode__(self):
		return str(self.numero)


class Inventario(models.Model):
	codigo = models.CharField(max_length=10, null=True, blank=True)
	quantidade = models.IntegerField()
	item = models.CharField(max_length=255)
	marca = models.CharField(max_length=100, null=True, blank=True)
	modelo = models.CharField(max_length=100, null=True, blank=True)
	descricao = models.TextField(null=True, blank=True)
	caixa = models.CharField(max_length=100)
	tags = models.ManyToManyField(Tag)
	
	class Meta:
		verbose_name = 'Item'
		verbose_name_plural = 'Itens'


	def __unicode__(self):
		return self.item


class Emprestimo(models.Model):
	responsavel = models.ForeignKey(User)
	item = models.ManyToManyField(Inventario)
	quantidade = models.IntegerField()
	status = models.CharField(max_length=10, choices=(
		('Emprestado', 'EMPRESTADO'),
		('Devolvido', 'DEVOLVIDO')
		))
	data_saida = models.DateTimeField()
	data_entrada = models.DateTimeField(null=True, blank=True)


	def __unicode__(self):
		return self.responsavel.first_name

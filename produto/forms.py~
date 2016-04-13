from django import forms
from .models import Produto, CompraProduto

class ProdutoForm(forms.ModelForm):
	class Meta:
		model = Produto
		fields = ['nome']

class RegistraCompraForm(forms.ModelForm):
	class Meta:
		model = CompraProduto
		fields = ['produto', 'qtd', 'preco']

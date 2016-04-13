from django.conf.urls import  url

from . import views

app_name='produto'
urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^produto/cadastrar', views.cadastrar, name='cadastrar'),
	url(r'^produto/listar', views.listar, name='listar'),
	url(r'^produto/registrarCompra', views.registrarCompra, name='registrar_compra'),
	url(r'^produto/compraRegistrada', views.listarRegistroCompras, name='compra_registrada'),
	url(r'^produto/filaProcessamento', views.filaProcessamento, name='fila_processamento')

]

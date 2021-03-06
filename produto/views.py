from django.shortcuts import render
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from produto.models import Produto, CompraProduto
from produto.forms import ProdutoForm, RegistraCompraForm
import threading



#Funcao Indice:
#Mostra Pro Usuario um Menu de produtos
def index (request):
    template = loader.get_template('produto/index.html')
    context ={}
    return HttpResponse(template.render(context,request))

def cadastrar (request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return listar(request)
    else:
        form = ProdutoForm()

    template = loader.get_template('produto/cadastrar.html')
    context = {'form' : form}
    return HttpResponse(template.render(context,request))

def listar (request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()

    produtos = Produto.objects.all()
    template = loader.get_template('produto/listar.html')
    context = {'produtos':produtos}
    return HttpResponse(template.render(context,request))

def listarRegistroCompras (request):
    if request.method == 'POST':
        form = RegistraCompraForm(request.POST)
        if form.is_valid():
            registro = form.save()
            thr = threading.Thread(target=registro.processarCompra, args=(), kwargs={})
            thr.start()
    registros = CompraProduto.objects.all()
    template = loader.get_template('produto/compraRegistrada.html')
    context = {'registros':registros}
    return HttpResponse(template.render(context,request))

def registrarCompra (request):
    if request.method == 'POST':
        form = RegistraCompraForm(request.POST)
        if form.is_valid():
            form.save()
            return listarRegistroCompras(request)
    else:
        form = RegistraCompraForm()
    template = loader.get_template('produto/registrarCompra.html')
    context = {'form' : form}
    return HttpResponse(template.render(context,request))

def filaProcessamento (request):
    processamentos = CompraProduto.objects.all()
    template = loader.get_template('produto/filaProcessamento.html')
    context = {'processamentos':processamentos}
    return HttpResponse(template.render(context,request))

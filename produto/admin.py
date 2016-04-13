from django.contrib import admin
from .models import Produto, CompraProduto

# Register your models here.

admin.site.register(Produto)
admin.site.register(CompraProduto)

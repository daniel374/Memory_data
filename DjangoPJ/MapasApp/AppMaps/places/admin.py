from django.contrib import admin
from django.contrib.admin import AdminSite
from django.db import models
# Register your models here.
from places.models import Localidades, Ciudades, Tipodocumentos, TiposInsumos, Perfiles, Clientes, Insumos, FormasPagos, OrdenesFacturas, Almacen, PagosOrdenes, Facturas, FacturasInsumos, PedidoInterno, Remisiones, Usuarios

class MyAdminSite(AdminSite):
    site_header = 'Monty Python administration'

admin_site = MyAdminSite(name='myadmin')

@admin.register(Localidades)
class LocalidadesAdmin(admin.ModelAdmin):
    list_display = ('cod_localidad', 'local_nombre')


admin.site.register(Ciudades)
admin.site.register(Tipodocumentos)
admin.site.register(TiposInsumos)
admin.site.register(Perfiles)
admin.site.register(Clientes)
admin.site.register(Insumos)
admin.site.register(FormasPagos)
admin.site.register(OrdenesFacturas)
admin.site.register(Almacen)
admin.site.register(PagosOrdenes)
admin.site.register(Facturas)
admin.site.register(FacturasInsumos)
admin.site.register(PedidoInterno)
admin.site.register(Remisiones)
admin.site.register(Usuarios)

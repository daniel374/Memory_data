from django.db import models

class Localidades(models.Model):
    cod_localidad = models.IntegerField(primary_key=True)
    local_nombre = models.CharField(db_column='Local_nombre', max_length=24, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
         return self.local_nombre

    class Meta:
        managed = False
        db_table = 'localidades'


class Ciudades(models.Model):
    cod_ciudad = models.IntegerField(primary_key=True)
    ciudad_nombre = models.CharField(max_length=24, blank=True, null=True)
    ciu_cod_localidad = models.ForeignKey('Localidades', models.DO_NOTHING, db_column='Ciu_cod_Localidad', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ciudades'


class Tipodocumentos(models.Model):
    tipodoc_id = models.CharField(db_column='TipoDoc_id', primary_key=True, max_length=2)  # Field name made lowercase.
    tipodoc_desc = models.CharField(db_column='TipoDoc_desc', max_length=24, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipodocumentos'


class TiposInsumos(models.Model):
    tpinsu_id = models.CharField(db_column='TpInsu_id', primary_key=True, max_length=10)  # Field name made lowercase.
    tpinsu_desc = models.CharField(db_column='TpInsu_desc', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipos_insumos'


class Perfiles(models.Model):
    perf_id = models.CharField(db_column='Perf_id', primary_key=True, max_length=3)  # Field name made lowercase.
    perf_nombre = models.CharField(db_column='Perf_nombre', max_length=10, blank=True, null=True)  # Field name made lowercase.
    perf_desc = models.CharField(db_column='Perf_desc', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'perfiles'


class Clientes(models.Model):
    cli_numdoc = models.CharField(db_column='Cli_numDoc', primary_key=True, max_length=15)  # Field name made lowercase.
    cli_nombre = models.CharField(db_column='Cli_nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cli_apellido = models.CharField(db_column='Cli_apellido', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cli_correo = models.CharField(db_column='Cli_correo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cli_telefono = models.IntegerField(db_column='Cli_telefono', blank=True, null=True)  # Field name made lowercase.
    cli_direccion = models.CharField(db_column='Cli_direccion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cli_perfil = models.ForeignKey('Perfiles', models.DO_NOTHING, db_column='Cli_perfil', blank=True, null=True)  # Field name made lowercase.
    cli_codciudad = models.ForeignKey(Ciudades, models.DO_NOTHING, db_column='Cli_codCiudad', blank=True, null=True)  # Field name made lowercase.
    cli_tipodoc = models.ForeignKey('Tipodocumentos', models.DO_NOTHING, db_column='Cli_TipoDoc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientes'


class Insumos(models.Model):
    insu_refer_id = models.CharField(db_column='Insu_refer_id', primary_key=True, max_length=15)  # Field name made lowercase.
    insu_nombre = models.CharField(db_column='Insu_nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    insu_desc = models.CharField(db_column='Insu_desc', max_length=45, blank=True, null=True)  # Field name made lowercase.
    insu_precio = models.IntegerField(db_column='Insu_precio', blank=True, null=True)  # Field name made lowercase.
    insu_precio_iva = models.IntegerField(db_column='Insu_precio_iva', blank=True, null=True)  # Field name made lowercase.
    insu_cant_almacen = models.IntegerField(db_column='Insu_cant_almacen', blank=True, null=True)  # Field name made lowercase.
    insu_tipo = models.ForeignKey('TiposInsumos', models.DO_NOTHING, db_column='Insu_tipo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'insumos'


class FormasPagos(models.Model):
    fp_id = models.CharField(db_column='FP_id', primary_key=True, max_length=3)  # Field name made lowercase.
    fp_descripcion = models.CharField(db_column='FP_descripcion', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'formas_pagos'


class OrdenesFacturas(models.Model):
    orden_compra = models.CharField(primary_key=True, max_length=15)
    desc_compra = models.CharField(max_length=45, blank=True, null=True)
    orden_fecha = models.DateField(blank=True, null=True)
    orden_valor_total = models.IntegerField(blank=True, null=True)
    orden_conse_factura = models.CharField(max_length=15, blank=True, null=True)
    orden_cli_numdoc = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='orden_Cli_numDoc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ordenes_facturas'

        
class Almacen(models.Model):
    al_id = models.CharField(db_column='Al_id', primary_key=True, max_length=4)  # Field name made lowercase.
    al_desc_insumo = models.CharField(db_column='Al_desc_insumo', max_length=45, blank=True, null=True)  # Field name made lowercase.
    al_cant_insumo = models.IntegerField(db_column='Al_cant_insumo', blank=True, null=True)  # Field name made lowercase.
    al_refer_insumo = models.OneToOneField('Insumos', models.DO_NOTHING, db_column='Al_refer_Insumo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'almacen'


class PagosOrdenes(models.Model):
    pg_orden_id = models.IntegerField(db_column='PG_orden_Id', primary_key=True)  # Field name made lowercase.
    pg_numero_cuotas = models.IntegerField(db_column='PG_numero_cuotas', blank=True, null=True)  # Field name made lowercase.
    pg_fecha = models.DateField(db_column='PG_fecha', blank=True, null=True)  # Field name made lowercase.
    pg_valor_total = models.IntegerField(db_column='PG_valor_total', blank=True, null=True)  # Field name made lowercase.
    pg_formas_pagos = models.ForeignKey(FormasPagos, models.DO_NOTHING, db_column='PG_formas_pagos', blank=True, null=True)  # Field name made lowercase.
    pg_factura = models.ForeignKey(OrdenesFacturas, models.DO_NOTHING, db_column='PG_factura', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pagos_ordenes'


class Facturas(models.Model):
    consecutivo_id = models.CharField(db_column='Consecutivo_id', primary_key=True, max_length=15)  # Field name made lowercase.
    desc_factura = models.CharField(max_length=45, blank=True, null=True)
    id_orden_compra = models.ForeignKey('OrdenesFacturas', models.DO_NOTHING, db_column='Id_orden_compra', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'facturas'


class FacturasInsumos(models.Model):
    fac_orden_compra = models.OneToOneField('OrdenesFacturas', models.DO_NOTHING, db_column='Fac_orden_compra', primary_key=True)  # Field name made lowercase.
    insu_refer = models.ForeignKey('Insumos', models.DO_NOTHING, db_column='Insu_refer_id')  # Field name made lowercase.
    cant_vendidas = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facturas_insumos'
        unique_together = (('fac_orden_compra', 'insu_refer'),)


class PedidoInterno(models.Model):
    pedint_id = models.CharField(db_column='pedInt_id', primary_key=True, max_length=15)  # Field name made lowercase.
    desc_pedido_interno = models.CharField(max_length=45, blank=True, null=True)
    id_orden_compra = models.ForeignKey(OrdenesFacturas, models.DO_NOTHING, db_column='Id_orden_compra', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pedido_interno'


class Remisiones(models.Model):
    remision_id = models.CharField(db_column='Remision_id', primary_key=True, max_length=15)  # Field name made lowercase.
    desc_remision = models.CharField(max_length=45, blank=True, null=True)
    id_orden_compra = models.ForeignKey(OrdenesFacturas, models.DO_NOTHING, db_column='Id_orden_compra', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'remisiones'


class Usuarios(models.Model):
    usu_numdoc = models.CharField(db_column='Usu_numDoc', primary_key=True, max_length=15)  # Field name made lowercase.
    usu_nombre = models.CharField(db_column='Usu_nombre', max_length=20, blank=True, null=True)  # Field name made lowercase.
    usu_correo = models.CharField(db_column='Usu_correo', max_length=15, blank=True, null=True)  # Field name made lowercase.
    usu_password = models.CharField(db_column='Usu_password', max_length=8, blank=True, null=True)  # Field name made lowercase.
    usu_tipodoc = models.ForeignKey(Tipodocumentos, models.DO_NOTHING, db_column='Usu_TipoDoc', blank=True, null=True)  # Field name made lowercase.
    usu_perfil = models.ForeignKey(Perfiles, models.DO_NOTHING, db_column='Usu_perfil', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'usuarios'

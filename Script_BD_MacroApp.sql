create database macro_app;
use macro_app;

create table localidades (
	cod_localidad int(2),
	Local_nombre varchar(24),
	primary key (cod_localidad)
);

create table ciudades (
	cod_ciudad int(4),
	ciudad_nombre varchar(24),
	Ciu_cod_Localidad int(2),
	primary key (cod_ciudad),
	foreign key (Ciu_cod_Localidad) references localidades (cod_Localidad)
);

create table tipoDocumentos (
	TipoDoc_id varchar(2),
	TipoDoc_desc varchar(24),
	primary key (TipoDoc_id)
);

create table tipos_insumos (
	TpInsu_id varchar(10),
	TpInsu_desc varchar(45),
	primary key (TpInsu_id)
);

create table perfiles (
	Perf_id varchar(3),
	Perf_nombre varchar(10),
	Perf_desc varchar(20),
	primary key (Perf_id)
);

create table clientes (
	Cli_numDoc varchar(15),
	Cli_nombre varchar(45),
	Cli_apellido varchar(45),
	Cli_correo varchar(45),
	Cli_telefono int(15),
	Cli_direccion varchar(45),
	Cli_perfil varchar(3),
	Cli_codCiudad int(4),
	Cli_TipoDoc varchar(2),
	primary key (Cli_numDoc),
	foreign key (Cli_codCiudad) references ciudades (cod_ciudad),
	foreign key (Cli_TipoDoc) references tipoDocumentos (TipoDoc_id),
	foreign key (Cli_perfil) references perfiles (Perf_id)
);

create table insumos (
	Insu_refer_id varchar(15),
	Insu_nombre varchar(45),
	Insu_desc varchar(45),
	Insu_precio int(15),
	Insu_precio_iva int(15),
	Insu_cant_almacen int(10),
	Insu_tipo  varchar(10),
	primary key (Insu_refer_id),
	foreign key (Insu_tipo) references tipos_insumos (TpInsu_id)
);

create table formas_pagos (
	FP_id varchar(3),
	FP_descripcion varchar(20),
	primary key (FP_id)
);

create table ordenes_facturas (
	orden_compra varchar(15),
	desc_compra varchar(45),
	orden_fecha date,
	orden_valor_total int(15),
	orden_conse_factura varchar(15),
	orden_Cli_numDoc varchar(15),
	primary key (orden_compra),
	foreign key (orden_Cli_numDoc) references clientes (Cli_numDoc)
);

create table almacen (
	Al_id varchar(4),
	Al_desc_insumo varchar(45),
	Al_cant_insumo int(10),
	Al_refer_Insumo varchar(15),
	primary key (Al_id),
	foreign key (Al_refer_Insumo) references insumos (Insu_refer_id)
);

create table pagos_ordenes (
	PG_orden_Id int(10),
	PG_numero_cuotas int(2),
	PG_fecha date,
	PG_valor_total int(10),
	PG_formas_pagos varchar(3),
	PG_factura varchar(15),
	primary key (PG_orden_Id),
	foreign key (PG_formas_pagos) references formas_pagos (FP_id),
	foreign key (PG_factura) references ordenes_facturas (orden_compra)
);

create table facturas (
	Consecutivo_id varchar(15),
	desc_factura varchar(45),
	Id_orden_compra varchar(15),
	primary key (Consecutivo_id),
	foreign key (Id_orden_compra) references ordenes_facturas (orden_compra)
);

create table facturas_insumos (
	Fac_orden_compra varchar(15),
	Insu_refer_id varchar(15),
	cant_vendidas int(10),
	primary key (Fac_orden_compra,Insu_refer_id),
	foreign key (Fac_orden_compra) references ordenes_facturas (orden_compra),
	foreign key (Insu_refer_id) references insumos (Insu_refer_id)
);

create table pedido_interno (
	pedInt_id varchar(15),
	desc_pedido_interno varchar(45),
	Id_orden_compra varchar(15),
	primary key (pedInt_id),
	foreign key (Id_orden_compra) references ordenes_facturas (orden_compra)
);

create table remisiones (
	Remision_id varchar(15),
	desc_remision varchar(45),
	Id_orden_compra varchar(15),
	primary key (Remision_id),
	foreign key (Id_orden_compra) references ordenes_facturas (orden_compra)
);


create table usuarios (
	Usu_numDoc varchar(15),
	Usu_nombre varchar(20),
	Usu_correo varchar(15),
	Usu_password varchar(8),
	Usu_TipoDoc varchar(2),
	Usu_perfil varchar(3),
	primary key (Usu_numDoc),
	foreign key (Usu_TipoDoc) references tipoDocumentos (TipoDoc_id),
	foreign key (Usu_perfil) references perfiles (Perf_id)
);
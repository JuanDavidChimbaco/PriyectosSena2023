from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

estadosMantenimiento = [
    ('Satisfactorio','Satisfactorio'),('Requiere Ajuste','Requiere Ajuste'),
    ('Requiere Reparacion','Requiere Reparacion'),('Requiere Reemplazo','Requiere Reemplazo'),
    ('Defecto Corregido','Defecto Corregido')
]
tipoProvedores=[
    ('Persona Juridica', 'Persona Juridica'),
    ('Persona Natural', 'Persona Natural')
]
tipoUsuario=[
    ('Instructor','Instructor'),
    ('Aprendiz','Aprendiz'),
    ('Administrativo', 'Administrativo')
]
tipoElemento = [
    ('Herramientas','Herramientas'),
    ('Maquinaria', 'Maquinaria'),
    ('Equipos', 'Equipos'),
    ('Materiales', 'Materiales')
]
estadosElementos = [
    ('Bueno', 'Bueno'),
    ('Regular','Regular'),
    ('Malo','Malo')
]
estadosSolicitudes = [
    ('Solicitada','Solicitada'),
    ('Aprobada','Aprobada'),
    ('Atendida','Atendida'),
    ('Cancelada','Cancelada')
]
class Ficha(models.Model):
    ficCodigo = models.IntegerField(unique=True,db_comment = "Codigo de la Ficha")
    ficNombre = models.CharField(max_length=100)
    fechaHoraCreacion = models.DateTimeField(auto_now_add=True)
    FechaHoraActualizacion = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.ficCodigo} - {self.ficNombre}"

class UnidadMedida(models.Model):
    uniNombre = models.CharField(max_length=45, unique=True)
    fechaHoraCreacion = models.DateTimeField(auto_now_add=True)
    FechaHoraActualizacion = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.uniNombre}"
    
class Proveedor(models.Model):
    proTipo = models.CharField(max_length=16, choices=tipoProvedores)
    proIdentificacion = models.CharField(max_length=45,unique=True)
    proNombre = models.CharField(max_length=45)
    proRepresentanteLegal = models.CharField(max_length=60,null=True)
    fechaHoraCreacion = models.DateTimeField(auto_now_add=True)
    FechaHoraActualizacion = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.proNombre}"  
    
class User(AbstractUser):
    userFoto = models.FileField(upload_to=f"fotos/", null=True, blank=True)
    userTipo = models.CharField(choices=tipoUsuario, max_length=15)
    fechaHoraCreacion = models.DateTimeField(auto_now_add=True )
    FechaHoraActualizacion = models.DateTimeField(auto_now=True )
    
    
class Elemento(models.Model):
    eleCodigo = models.CharField(max_length=15, unique=True)
    eleNombre = models.CharField(max_length=50)
    eleTipo = models.CharField(choices=tipoElemento, max_length=12)
    eleEstado = models.CharField(choices=estadosElementos, max_length=50)
    fechaHoraCreacion = models.DateTimeField(auto_now_add=True)
    FechaHoraActualizacion = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.eleCodigo} - {self.eleNombre}"
    
class Devolutivo(models.Model):
    devPlacaSena = models.CharField(null=True, max_length=50)
    devSerial = models.CharField(null=True, max_length=50)
    devDescripcion = models.TextField()
    devMarca = models.CharField(null=True, max_length=50)
    devFechaIngresoSena = models.DateField()
    devValor = models.DecimalField(max_digits=5, decimal_places=2)
    devFoto = models.FileField(upload_to=f"elementos/", null=True, blank=True)
    devElemento = models.ForeignKey(Elemento, on_delete=models.PROTECT)
    fechaHoraCreacion = models.DateTimeField( auto_now_add=True)
    FechaHoraActualizacion = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.devElemento
    
class Material(models.Model):
    matReferencia = models.TextField(null=True)
    matMarca = models.CharField(max_length=50, null=True)
    matUnidadMedida = models.ForeignKey(UnidadMedida, on_delete=models.PROTECT)
    matElemento = models.ForeignKey(Elemento, on_delete=models.PROTECT)
    fechaHoraCreacion = models.DateTimeField( auto_now_add=True)
    FechaHoraActualizacion = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.matElemento}"
    
class EntradaMaterial(models.Model):
    entNumeroFactura = models.CharField(max_length=15)
    entUsuarioRecibe = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    entFechaHora = models.DateTimeField(default=datetime.now())
    entEntregadoPor = models.CharField(max_length=100)
    entObservaciones = models.TextField(null=True)
    entProveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    fechaHoraCreacion = models.DateTimeField( auto_now_add=True)
    FechaHoraActualizacion = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.entNumeroFactura}"
    
class DetalleEntradaMateriales(models.Model):
    detEntradaMaterial = models.ForeignKey(EntradaMaterial, on_delete=models.PROTECT)
    detMaterial = models.ForeignKey(Material, on_delete=models.PROTECT)
    detCantidad = models.IntegerField()
    detPrecioUnitario = models.FloatField()
    detEstado = models.CharField(choices=estadosElementos, max_length=7)
    fechaHoraCreacion = models.DateTimeField( auto_now_add=True)
    FechaHoraActualizacion = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.detMaterial} -> {self.detCantidad}"
    
class SolicitudElemento(models.Model):
    solUsuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    solFicha = models.ForeignKey(Ficha, on_delete=models.PROTECT)
    solProyecto = models.CharField(max_length=500)
    solFechaHoraRequerida = models.DateTimeField(null=True)
    solEstado = models.CharField(choices=estadosSolicitudes, max_length=10)
    solObservaciones = models.TextField(null=True)
    fechaHoraCreacion = models.DateTimeField( auto_now_add=True)
    FechaHoraActualizacion = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.solUsuario} - {self.solFicha} - {self.solProyecto}"
    
class DetalleSolicuitud(models.Model):
    detSolicitud = models.ForeignKey(SolicitudElemento, on_delete=models.PROTECT)
    detElemento = models.ForeignKey(Elemento, on_delete=models.PROTECT)
    detUnidadMedida = models.ForeignKey(UnidadMedida, on_delete=models.PROTECT)
    detCantidadRequerida = models.IntegerField()
    fechaHoraCreacion = models.DateTimeField( auto_now_add=True)
    FechaHoraActualizacion = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.detElemento} - {self.detCantidadRequerida}"
    
class SalidaDetalleSolicitud(models.Model):
    salDetalleSolicitud = models.ForeignKey(DetalleSolicuitud, on_delete=models.PROTECT)
    salCantidadEntregada = models.IntegerField()
    salObservaciones = models.TextField(null=True)
    fechaHoraCreacion = models.DateTimeField( auto_now_add=True)
    FechaHoraActualizacion = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.salDetalleSolicitud} -> {self.salCantidadEntregada}"
    
class DevolucionElemento(models.Model):
    devSalida = models.ForeignKey(SalidaDetalleSolicitud, on_delete=models.PROTECT) # devDetalleSalida
    devUsuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    devCantidadDevoluicion = models.IntegerField()
    devObservaciones = models.TextField(null=True)
    fechaHoraCreacion = models.DateTimeField( auto_now_add=True)
    FechaHoraActualizacion = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.devSalida} -> {self.devCantidadDevoluicion}"
    
class EstadoMantenimiento(models.Model):
    estNombre = models.CharField(max_length=50, unique=True, choices=estadosMantenimiento)
    fechaHoraCreacion = models.DateTimeField( auto_now_add=True)
    FechaHoraActualizacion = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.estNombre}"
    
class Mantenimientos(models.Model):
    manElemento = models.ForeignKey(Elemento, on_delete=models.PROTECT)
    manPersona = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    manEstado = models.ForeignKey(EstadoMantenimiento, on_delete=models.PROTECT)
    manObservaciones = models.TextField(null=True)
    manFechaHoraMantenimiento = models.DateTimeField()
    fechaHoraCreacion = models.DateTimeField( auto_now_add=True)
    FechaHoraActualizacion = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.manElemento} - {self.manEstado}"

class UbicacionFisica(models.Model):
    ubiElemento = models.ForeignKey(Elemento, on_delete=models.PROTECT)
    ubiDeposito = models.IntegerField()
    ubiEstante = models.IntegerField(null=True)
    ubiEntrepano = models.IntegerField(null=True)
    ubiLocker = models.SmallIntegerField()
    fechaHoraCreacion = models.DateTimeField( auto_now_add=True)
    FechaHoraActualizacion = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.ubiDeposito} {self.ubiEstante} {self.ubiEntrepano} {self.ubiElemento}" 
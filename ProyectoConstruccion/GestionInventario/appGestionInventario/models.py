from django.db import models

# Create your models here.
tipoProvedores=[
    ('PJ', 'Persona Juridica'),
    ('PN', 'Persona Natural')
]
tipoPersona=[
    ('IN','Instructor'),
    ('AP','Aprendiz')
]
tipoElemento = [
    ('MAT', 'Materiales'),
    ('HER','Herramientas'),
    ('MAQ', 'Maquinaria'),
    ('EQU', 'Equipos')
]
EstadoRoles = [
    ('ACT','Activo'),
    ('INA', 'Inactivo')
]
devEstados = [
    ('B', 'Bueno'),
    ('R','Regular'),
    ('M','Malo')
]
detEstados = [
    ('B', 'Bueno'),
    ('R','Regular'),
    ('M','Malo')
]
solEstados = [
    ('SOL','Solicitada'),
    ('APR','Aprobada'),
    ('ATE','Atendida'),
    ('CAN','Cancelada')
]

class UnidadMedida(models.Model):
    uniNombre = models.CharField(max_length=45, unique=True , help_text="Nombre de la Unidad de medida")
    def __str__(self) -> str:
        return self.uniNombre
    
class Persona(models.Model):
    perIdentificacion = models.CharField(max_length=45,unique=True)
    perNombres = models.CharField(max_length=45)
    perApellidos = models.CharField(max_length=45)
    perEmail = models.EmailField(max_length=60, unique=True)
    perTipo = models.CharField(max_length=2,choices=tipoPersona)
    def __str__(self) -> str:
        return self.perNombres
    
class Usuarios(models.Model):
    usuLogin = models.CharField(max_length=45)
    usuPassword = models.CharField(max_length=60)
    usuPersona = models.ForeignKey(Persona, help_text="esta es la llave foranea", on_delete=models.DO_NOTHING)
    def __str__(self) -> str:
        return self.usuLogin
    
class Rol(models.Model):
    rolNombre = models.CharField(max_length=45,unique=True)
    def __str__(self) -> str:
        return self.rolNombre
    
class UsuariosRoles(models.Model):
    usuUsuario = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING)
    usuRol = models.ForeignKey(Rol, on_delete=models.DO_NOTHING)
    usuEstado = models.CharField(choices=EstadoRoles , max_length=3, null=True)
    def __str__(self) -> str:
        return self.usuEstado
    
class Proveedor(models.Model):
    proTipo = models.CharField(max_length=2, choices=tipoProvedores)
    proIdentificacion = models.CharField(max_length=45,unique=True)
    proNombre = models.CharField(max_length=45)
    proRepresentanteLegal = models.CharField(max_length=60,null=True)
    def __str__(self) -> str:
        return self.proNombre
    
class Fichas(models.Model):
    ficCodigo = models.IntegerField(unique=True)
    ficNombre = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.ficNombre
    
class Elementos(models.Model):
    eleRadicado = models.CharField(max_length=15, unique=True)
    eleTipo = models.CharField(choices=tipoElemento, max_length=3)
    eleFechaHoraRegistro = models.DateTimeField(auto_now=False, auto_now_add=False)
    def __str__(self) -> str:
        return self.eleRadicado
    
class Devolutivos(models.Model):
    devPlacaSena = models.CharField(null=True, max_length=50)
    devSerial = models.CharField(null=True, max_length=50)
    devDescripcion = models.CharField(max_length=200)
    devMarca = models.CharField(null=True, max_length=50)
    devFechaIngresoSena = models.DateField(auto_now=False, auto_now_add=False)
    devValor = models.FloatField()
    devEstado = models.CharField(choices=devEstados , max_length=1)
    devFoto = models.CharField(null=True, max_length=50)
    devElemento = models.ForeignKey(Elementos, on_delete=models.DO_NOTHING)
    def __str__(self) -> str:
        return self.devDescripcion
    
class UbicacionFisica(models.Model):
    ubiElemento = models.ForeignKey(Elementos, on_delete=models.DO_NOTHING)
    ubiDeposito = models.IntegerField()
    ubiEstante = models.IntegerField()
    ubiEntrepano = models.IntegerField()
    def __str__(self) -> str:
        return self.ubiDeposito
    
class Materiales(models.Model):
    matNombre = models.CharField(max_length=50)
    matReferencia = models.CharField(max_length=100, null=True)
    matMarca = models.CharField(max_length=50)
    matUnidadMedida = models.ForeignKey(UnidadMedida, on_delete=models.DO_NOTHING)
    matElemento = models.ForeignKey(Elementos, on_delete=models.DO_NOTHING)
    def __str__(self) -> str:
        return self.matNombre
    
class EstadoMantenimiento(models.Model):
    estNombre = models.CharField(max_length=50, unique=True)
    def __str__(self) -> str:
        return self.estNombre
    
class Mantenimientos(models.Model):
    manElemento = models.ForeignKey(Elementos, on_delete=models.DO_NOTHING)
    manPersona = models.ForeignKey(Persona,on_delete=models.DO_NOTHING)
    manEstado = models.ForeignKey(EstadoMantenimiento, on_delete=models.DO_NOTHING)
    manObservaciones = models.TextField(null=True)
    manFechaHora = models.DateTimeField(auto_now=False, auto_now_add=False)
    
class EntradaMateriales(models.Model):
    entNumeroFactura = models.CharField(max_length=15)
    entPersonaRecibe = models.ForeignKey(Persona, on_delete=models.DO_NOTHING)
    entFechaHora = models.DateTimeField( auto_now=False, auto_now_add=False)
    entEntregadoPor = models.CharField(max_length=100)
    entObservaciones = models.CharField(max_length=400,null=True)
    entProveedor = models.ForeignKey(Proveedor, on_delete=models.DO_NOTHING)
    def __str__(self) -> str:
        return self.entNumeroFactura
    
class DetalleEntradaMateriales(models.Model):
    detEntradaMaterial = models.ForeignKey(EntradaMateriales, on_delete=models.DO_NOTHING)
    detMaterial = models.ForeignKey(Materiales, on_delete=models.DO_NOTHING)
    detCantidad = models.IntegerField()
    detPrecioUnitario = models.FloatField()
    detEstado = models.CharField(choices=detEstados, max_length=1)
    
class SolicitudElementos(models.Model):
    solFechaHora = models.DateTimeField(auto_now=False, auto_now_add=False)
    solPersona = models.ForeignKey(Persona, on_delete=models.DO_NOTHING)
    solFicha = models.ForeignKey(Fichas, on_delete=models.DO_NOTHING)
    solProyecto = models.CharField(max_length=500)
    solEstado = models.CharField(choices=solEstados, max_length=3, default=solEstados[0])
    solObservaciones = models.TextField(null=True,default='null')
    def __str__(self) -> str:
        return self.solProyecto
    
class DetalleSolicuitudes(models.Model):
    detSolicitud = models.ForeignKey(SolicitudElementos, on_delete=models.DO_NOTHING)
    detElemento = models.ForeignKey(Elementos, on_delete=models.DO_NOTHING)
    detCantidadRequerida = models.IntegerField()
    def __str__(self) -> str:
        return self.detCantidadRequerida
    
class SalidaDetalleSolicitud(models.Model):
    salDetalleSolicitud = models.ForeignKey(DetalleSolicuitudes, on_delete=models.DO_NOTHING)
    salCantidadEntregada = models.IntegerField()
    salFechaHora = models.DateTimeField(auto_now=False, auto_now_add=False)
    salObservaciones = models.CharField(max_length=400, null=True)
    def __str__(self) -> str:
        return self.salCantidadEntregada
    
class DevolucionElementos(models.Model):
    devSalida = models.ForeignKey(SalidaDetalleSolicitud, on_delete=models.DO_NOTHING)
    devPersona = models.ForeignKey(Persona, on_delete=models.DO_NOTHING)
    devCantidadEntregada = models.IntegerField()
    devFechaHora = models.DateTimeField(auto_now=False, auto_now_add=False)
    devObservaciones = models.TextField(null=True)
    def __str__(self) -> str:
        return self.devCantidadEntregada

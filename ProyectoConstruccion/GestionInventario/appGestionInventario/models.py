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

class UnidadMedida(models.Model):
    uniNombre = models.CharField(max_length=45, unique=True , help_text="Nombre de la Unidad de medida")
    def __str__(self) -> str:
        return self.uniNombre
    
class Rol(models.Model):
    rolNombre = models.CharField(max_length=45,unique=True)
    def __str__(self) -> str:
        return self.rolNombre
    
class Proveedor(models.Model):
    proTipo = models.CharField(max_length=2, choices=tipoProvedores)
    proIdentificacion = models.CharField(max_length=45,unique=True)
    proNombre = models.CharField(max_length=45)
    proRepresentanteLegal = models.CharField(max_length=60,null=True)
    def __str__(self) -> str:
        return self.proNombre
    
class Persona(models.Model):
    perIdentificacion = models.CharField(max_length=45,unique=True)
    perNombres = models.CharField(max_length=45)
    perApellidos = models.CharField(max_length=45)
    perEmail = models.EmailField(max_length=60, unique=True)
    perTipo = models.CharField(max_length=2,choices=tipoPersona)
    def __str__(self) -> str:
        return self.perNombres
    
class Fichas(models.Model):
    ficCodigo = models.IntegerField(unique=True)
    ficNombre = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.ficNombre
    
class Usuarios(models.Model):
    usuLogin = models.CharField(max_length=45)
    usuPassword = models.CharField(max_length=60)
    usuPersona = models.ForeignKey(Persona, help_text="esta es la llave foranea", on_delete=models.DO_NOTHING)
    def __str__(self) -> str:
        return self.usuLogin
    
class UbicacionFisica(models.Model):
    ubiElemento = models.IntegerField()
    ubiDeposito = models.IntegerField()
    ubiEstante = models.IntegerField()
    ubiEntrepano = models.IntegerField()
    def __str__(self) -> str:
        return self.ubiElemento
    

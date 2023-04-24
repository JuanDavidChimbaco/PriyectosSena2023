from django.db import models

# Create your models here.
tipoProveedores=[
    ('PJ','Persona Juridica'),
    ('PN','Persona Natural')
]
tipoPersona = [
    ('IN','Instructor'),
    ('AP','Aprendiz')
]

class UnidadMedida(models.Model):
    uniNombre = models.CharField(max_length=45,unique=True,verbose_name = "nombre de la unidad de medida", help_text="nombre de la unidad de medida2")
    
    def __str__(self) -> str:
        return self.uniNombre
    
class Rol(models.Model):
    rolNombre = models.CharField(max_length=45,unique=True)
    
    def __str__(self) -> str:
        return self.rolNombre
    
class proveedor(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _str_: _nombre de los probedores_
    """
    proTipo = models.CharField(max_length=2,choices=tipoProveedores)
    proIdentificacion = models.CharField(max_length=45,unique=True)
    proNombre = models.CharField(max_length=45)
    proRepresentanteLegal = models.CharField(max_length=60,null=True)
    
    def __str__(self) -> str:
        return self.proNombre
    
class Persona(models.Model):
    perIndentificacion = models.CharField(max_length=15,unique=True)
    perNombres = models.CharField(max_length=45)
    perApellidos = models.CharField(max_length=45)
    perEmail = models.EmailField(max_length=60,unique=True)
    perTipo = models.CharField(max_length=3,choices=tipoPersona)
    
    def __str__(self) -> str:
        return f"{self.perNombres} {self.perApellidos}"
    
class Fichas(models.Model):
    ficCodigo = models.IntegerField(unique=True)
    ficNombre = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.ficNombre
    
class Usuarios(models.Model):
    usuLogin = models.CharField(max_length=45)
    usuPassword = models.CharField(max_length=60)
    usuPersona = models.ForeignKey(Persona, verbose_name=_(""), on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return self.usuLogin
    
class UbicacionFisica(models.Model):
    ubiElemento = models.IntegerField()
    ubiDeposito = models.IntegerField()
    ubiEstante = models.IntegerField()
    ubiEntrepano = models.IntegerField()
    
    def __str__(self) -> str:
        return self.ubiElemento
    
    
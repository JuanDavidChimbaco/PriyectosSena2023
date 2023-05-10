from django.shortcuts import render , redirect
from django.db import Error, transaction
from django.contrib.auth.models import Group
import random
import string


# Create your views here.

def registrarUsuario(request):
    try:
      nombres = request.POST["txtNombres"]
      apellidos = request.POST["txtApellidos"]
      correo = request.POST["txtCorreo"]
      tipo = request.POST["cbTipo"]
      foto = request.FILE.get["fileFoto",False]
      idRol = int (request.POST["cbRol"])
      with transaction.atomic():
        #crea un objeto de tipo user
        user = User(username=correo,first_name=nombres,last_name=apellidos,email = correo, userTipo = tipo , userFoto = foto)
        user.save()
        # obtener el rol deacuerdo al id del rol
        rol = Group.objects.get(pk=idRol)
        # agregar usuarios a ese rol 
        user.groups.add(rol)
        # si el rol es administrativo se habilita que tenga acceso al sitio web del administrado 
        if(rol.name=="Administrado"):user.is_staff(True)
        # guardamos el usuario con lo que tenemos
        user.save()
        # llamamos a la funcxion generarPassword 
        passwordGenerado = generarPassword()
        print(f"password {passwordGenerado}")
        user.set_password(passwordGenerado)
        user.save()
        mensaje = "Usuario Agregado Correctamente"
        retorno = {"mensaje":mensaje}
        # enviar correo al usuario
        return redirect("/vistaGestionUsuarios/",retorno)
    except Error as error:
      transaction.rollback()
      mensaje = f"{error}"
    retorno = {"mensaje":mensaje, "user": user}
    return render(request, "admin/frmRegistrarUsuario.html",retorno)
  
def generarPassword():
  """_summary_
    Genera un password de longitud 10 que incluye 
    letras mayusculas y minusculas, digitos y caracteres espesciales
  Returns:
    _str_:retorna un password
  """
  longitud = 10
  caracteres = string.ascii_lowercase + string.ascii_uppercase \
              + string.digits + string.punctuation
  password = ''
  for i in range(longitud):
    password += ''.join(random.choice(caracteres))
  return password

def vistaRegistrarUsuario(request):
  roles = Group.objects.all()
  retorno = {"roles":roles, "user":None}
  return render(request, "admin/frmRegistrarUsuario.html", retorno)

from django.shortcuts import render , redirect
from appTienda.models import Categoria, Producto
from django.db import Error
import os

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def vistaCategorias(request):
    return render(request, 'frmAgregarCategoria.html')

def agregarCategorias(request):
    nombre = request.POST['txtCategoria']
    try:
        categoria = Categoria(catNombre=nombre)
        categoria.save()
        mensaje="Categoria Agregada Correctamente"
    except Error as error:
        mensaje=f"Problemas a la hora de agregar la categoria{error}"
    retorno = {"mensaje":mensaje}
    return render(request,"listarProductos.html",retorno)

def listarProductos(request):
    try:
        productos = Producto.objects.all()
        mensaje = ""
        print(productos)
    except Error as error:
        mensaje=f"Problemas al obtener Productos {error}"
    retorno={"mensaje":mensaje,"listaProductos":productos}
    return render(request,'listarProductos.html',retorno)

def vistaProducto(request):
    try:
        categorias = Categoria.objects.all()
        mensaje=""
    except Error as error:
        mensaje=f"Problemas al obtener las categorias{error}"
    retorno = {"mensaje":mensaje, "listaCategorias":categorias, "producto":None}
    return render(request, "frmAgregarProducto.html", retorno)

def agregarProducto(request):
    codigo = int(request.POST["txtCodigo"])
    nombre = request.POST["txtNombre"]
    precio = int(request.POST["txtPrecio"])
    idcategoria = int(request.POST["cbCategoria"])
    archivo = request.FILES['fileFoto']
    try:
        # obtener la categoria deacuerod a su id 
        categoria = Categoria.objects.get(id=idcategoria)
        # crear el producto
        producto = Producto(proCodigo=codigo,
                            proNombre=nombre,
                            proPrecio=precio,
                            proCategoria=categoria,
                            proFoto = archivo)

        # registrar el producto en la base de datos
        producto.save()
        mensaje = "Producto Agregado Correctamente"
        return redirect("/listarProductos/")
    
    except Error as error:
        mensaje = f"Problemas al agregar un producto. {error}"
        
    # obtener categorias 
    categorias = Categoria.objects.all()
    retorno = {"mensaje":mensaje, "listaCategorias":categorias, "prodcuto":producto}
    
    return render(request, "frmAgregarProducto.html",retorno)

def consultarProducto(request,id):
    try:
        producto = Producto.objects.get(id=id)
        print(producto.proCategoria_id)
        listaCategoria = Categoria.objects.all()
        mensaje=""
    except Error as error:
        mensaje = f"Problemas {error}"
    retorno = {"mensaje": mensaje, "producto": producto, "listaCategorias": listaCategoria}
    return render(request, "frmActualizarProducto.html", retorno)

def actualizarProducto(request):
    try:
        idProducto = int(request.POST["idProducto"])
        idCategoria = int(request.POST["cbCategoria"])
        
        categoria = Categoria.objects.get(id=idCategoria)
        
        producto = Producto.objects.get(id=idProducto)
        producto.proCodigo = request.POST["txtCodigo"]
        producto.proNombre = request.POST["txtNombre"]
        producto.proPrecio = request.POST["txtPrecio"]
        producto.proCategoria = categoria
        archivo = request.FILES.get('fileFoto',False)
        
        if(archivo!= False):
            producto.proFoto=archivo
        producto.save()
        mensaje = "Producto Actualizado"
        return redirect("/listarProductos")
        
    except Error as error:
        mensaje = f"provlemas al Actualizar{error}"
    categorias = Categoria.objects.all()
    retorno = {"mensaje":mensaje, "listaCategorias": categorias, "producto":producto}
    return render(request, "listarProductos.html", retorno)

def eliminarProducto(request,id):
    try:        
        producto = Producto.objects.get(id=id)
        if producto.proFoto:
            if os.path.exists(producto.proFoto.path):
                os.remove(producto.proFoto.path)
            producto.proFoto.delete()
        producto.delete()
        mensaje="Producto Eliminado"
         
    except Error as error:
        mensaje=f"Problemas al eliminar producto {error}"
    retorno = {"mensaje":mensaje,} 
    return redirect("/listarProductos/", retorno)
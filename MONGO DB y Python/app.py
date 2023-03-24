import pymongo
import os
#se crea objeto conexion al servidor mongodb
miConexion = pymongo.MongoClient('mongodb://localhost:27017')

#acceso a la base de datos
baseDatos = miConexion["Tiendaadso2449133"]
print(type(baseDatos))

#crear objeto que permite acceder a la coleccion productos

productos = baseDatos["productos"]
print(type(productos))

def agregarProducto():
    
    try:
        #aquí datos quemados prodian ser solicitados
        codigo = int(input("Escriba el código para agregar: "))
        nombre = input("Escriba el nombre del producto: ")
        categoria = input("Escriba la categoria del producto: ")
        precio = int(input("Escriba el precio del producto: "))
        
        #crear producto de tipo diccionario
        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio
        }
        
        existe = consultarProductoCodigo(codigo)
        if(existe):
            print("Ya existe producto con ese código. ")
            
        else:
            resultado = productos.insert_one(producto)
            print("Producto agregado correctamente. ")
            
    except pymongo.errors as error:
        print(error)
        
        
def consultarProductoCodigo(codigo):
    try:
        consulta = {"codigo": codigo}
        producto = productos.find_one(consulta)
        if(producto is not None):
            return True
        else:
            return False
        
    
    except pymongo.errors as error:
        print(error)
        return False
        

def consultarProducto():
    try:
        
        codigoConsultar = int(input("Escriba el código del producto: "))
        consulta = {"codigo": codigoConsultar}
        producto = baseDatos.productos.find_one(consulta)
        
        if(producto is not None):
            print("-----Datos del producto-----")
            print(producto)
            print(f"código: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Categoria: {producto['categoria']}")
            print(f"Precio: {producto['precio']}")
        else:
            print("Producto no encontrado")
    
    except pymongo.errors as error:
        print(error)
        
def actualizarProducto():
    try:
        codigoProducto = int(input("Digite el código del producto: "))
        #criterio para saber que producto se va a actualizar
        criterio = {"codigo": codigoProducto }
        #Aquí se crea un diccionario con los datos a actualizar
        codigo = int(input("Escriba el código para actualizar: "))
        nombre = input("Escriba el nuevo nombre del producto: ")
        categoria = input("Escriba la categoria del producto: ")
        precio = int(input("Escriba el precio del producto: "))
        
        datosActualizar = {
            "codigo": codigo,
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio
        }
        consulta = { "$set" : datosActualizar}
        resultado = baseDatos.productos.update_one(criterio,consulta)
        print("Producto actualizado. ")
        
    except pymongo.errors as error:
        print(error)

def eliminarProducto():
    try:
        codigoProducto = int(input("Digite el código del producto: "))
        
        consulta = {"codigo": codigoProducto}
        #eliminar
        baseDatos.productos.delete_one(consulta)
        #verificar despues si existe
        producto = baseDatos.productos.find_one(consulta)
        if(producto is None):
            print("Producto eliminado correctamente. ")
        else:
            print("No se ha podido eliminar el producto. ")
        
    except pymongo.errors as error:
        print(error)
        
def listarProductos():
    try:
        listarProductos = baseDatos.productos.find()
        for producto in listarProductos:
            print("-----Datos del producto-----")
            
            print(f"código: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Categoria: {producto['categoria']}")
            print(f"Precio: {producto['precio']}")
        
    except pymongo.errors as error:
        print(error)
    


def menu():
    while(True):
        os.system("cls")
        print("")
        print("1) Agregar Producto.")
        print("2) Consultar Producto.")
        print("3) Actualizar Producto.")
        print("4) Eliminar Productos.")
        print("5) Listar Productos.")
        print("6) Salir.")
        
        opcion = int(input("Digite una opcion de (1-6): "))
        if(opcion==1):
            agregarProducto()
        elif(opcion==2):
            consultarProducto()
        elif(opcion==3):
            actualizarProducto()
        elif(opcion==4):
            eliminarProducto()
        elif(opcion==5):
            listarProductos()
        elif(opcion==6):
            print("Hasta Pronto. ")
            break
        else:
            print("Opcion no válida. ")
        
        input("Presione Enter para continuar. ")
        
        
menu()
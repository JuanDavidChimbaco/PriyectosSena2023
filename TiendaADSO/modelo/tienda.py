from modelo.producto import Producto
from modelo.cliente import Cliente
from modelo.venta import Venta

class Tienda():
    
    def __init__(self):
        self.__listaClientes=[]
        self.__listaProductos=[]
        self.__listaVentas=[]
        
    def agregarProducto(self,producto=Producto):
        self.__listaProductos.append(producto)
        
    def agregarCliente(self,cliente=Cliente):
        self.__listaClientes.append(cliente)
        
    def agregarVenta(self,venta=Venta):
        self.__listaVentas.append(venta)
        
    def getListaClientes(self):
        return self.__listaClientes
    
    def getListaProductos(self):
        return self.__listaProductos
    
    def getListaVentas(self):
        return self.__listaVentas
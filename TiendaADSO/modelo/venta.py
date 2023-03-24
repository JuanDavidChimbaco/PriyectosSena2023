from modelo.detalleVenta import DetalleVenta
from modelo.cliente import Cliente
from modelo.producto import Producto
from datetime import datetime

class Venta():
    
    def __init__(self,cliente=Cliente):
        self.__cliente=cliente
        self.__fecha=datetime.now()
        self.__listaDetalle=[]
        
    def getCliente(self):
        return self.__cliente
    
    def getFecha(self):
        return self.__fecha
    
    def getListaDetalle(self):
        return self.__listaDetalle
    
    def agregarDetalleVenta(self,producto=Producto,cantidad=int):
        detalleVenta = DetalleVenta(producto,cantidad)
        self.__listaDetalle.append(detalleVenta)
        
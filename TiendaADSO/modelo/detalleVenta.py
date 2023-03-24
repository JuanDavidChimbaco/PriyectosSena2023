from modelo.producto import Producto

class DetalleVenta():
    
    def __init__(self,producto=Producto, cantidad=int):
        self.__producto=producto
        self.__cantidad=cantidad
        self.__valor=self.__producto.getPrecio()*self.__cantidad
        
    def getProducto(self):
        return self.__producto
    
    def getCantidad(self):
        return self.__cantidad
    
    def getValor(self):
        return self.__valor
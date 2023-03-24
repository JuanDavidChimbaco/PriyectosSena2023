from producto import Producto

class DetalleVenta():
    def __init__(self,cantidad=int,producto=Producto):
        self.__cantidad = cantidad
        self.__valorDetalle = self.__producto.getPrecio()*self.__cantidad
        self.__producto=producto
            
        
    @property
    def getCantidad(self):
        return self.__cantidad
    def getValor(self):
        return self.__valorDetalle
    def getProducto(self):
        return self.__producto
    
    @property
    def setCantidad(self,cantidad):
        self.cantidad = cantidad
    def setValor(self,valor):
        self.valor = valor
    def setProducto(self,producto):
        self.producto = producto
class Producto():
    
    def __init__(self,codigo=int, nombre=str,precio=int):
        """_summary_
            Constructor de Producto con parámetros
        Args:
            codigo (_type_, Entero): Código del producto. Identificador único. Defaults to int.
            nombre (_type_, String): Nombre del producto. Defaults to str.
            precio (_type_, Entero): Precio del producto. Defaults to int.
        """
        self.__codigo=codigo
        self.__nombre=nombre
        self.__precio=precio
        
    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre
    
    def getPrecio(self):
        return self.__precio
    
    def setCodigo(self,codigo):
        self.__codigo=codigo
        
    def setNombre(self,nombre):
        self.__nombre=nombre
        
    def setPrecio(self,precio):
        self.__precio=precio
        
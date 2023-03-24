class Cliente():
    
    def __init__(self,identificacion=str,nombre=str,direccion=str,correo=str):
        self.__identificacion=identificacion
        self.__nombre=nombre
        self.__direccion=direccion
        self.__correo=correo
        
    def getIdentificacion(self):
        return self.__identificacion
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getCorreo(self):
        return self.__correo
    
    def setIdentificacion(self,identificacion):
        self.__identificacion=identificacion
    
    def setNombre(self,nombre):
        self.__nombre=nombre
        
    def setDireccion(self,direccion):
        self.__direccion=direccion
        
    def setCorreo(self,correo):
        self.__correo=correo
        
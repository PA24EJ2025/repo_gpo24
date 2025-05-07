class Producto:
    def __init__(self,clave,descripcion):
        self.__clave = clave
        self.__descripcion = descripcion
    
    @property
    def clave(self):
        return self.__clave

    @clave.setter
    def clave(self,nuevo):
        self.__clave = nuevo

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self,nuevo):
        self.__descripcion = nuevo

    def desc_corta(self):
        return self.__descripcion[0:10] + "..."

    def desc_mayus(self):
        return self.__descripcion.upper()
    
objeto = Producto(1,"SmartTV")
    
objeto.clave = 21
objeto.descripcion = "Refri samsung 10 pies"
print(f"{objeto.clave},{objeto.desc_mayus()}")
print(f"{objeto.desc_corta()}")
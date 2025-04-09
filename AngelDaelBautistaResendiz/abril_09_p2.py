class Mi_clase:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def sumar(self):
        return self.num1 + self.num2 + self.num3
    
    def mayor(self): 
        nuevomayor = [self.num1, self.num2, self.num3]
        nuevomayor2= sorted(nuevomayor, reverse=True)
        return nuevomayor2

    def menor(self):
        pass

    def iguales(self):
        pass

    def concatenar(self):
        pass
        
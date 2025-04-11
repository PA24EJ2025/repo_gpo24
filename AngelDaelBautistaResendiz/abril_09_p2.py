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
        nuevomenor = [self.num1, self.num2, self.num3]
        nuevomenor2 = sorted(nuevomenor)
        return nuevomenor2 

    def iguales(self):
        return (self.num1 == self.num2) or (self.num1 == self.num3) or (self.num2 == self.num3)

    def concatenar(self):
        return str(self.num1) + str(self.num2) + str(self.num3)
        
objeto = Mi_clase(25, 25, 50)

print(f"Suma de todos los tres numeros: {objeto.sumar()}")
print(f"Numero Mayor: {objeto.mayor()}")
print(f"Numero Menor: {objeto.menor()}")
print(f"Hay iguales?: {objeto.iguales()}")
print(f"Numeros a cadena: {objeto.concatenar()}") 
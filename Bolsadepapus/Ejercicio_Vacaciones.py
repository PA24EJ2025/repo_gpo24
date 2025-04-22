# Clase
class Numeros:
    def __init__(self, numero1, numero2, numero3):
        self.numero1 = numero1
        self.numero2 = numero2
        self.numero3 = numero3

        #Sumar
    def sumar(self):
        return self.numero1 + self.numero2 + self.numero3
        #Numero MAyor
    def mayor(self):
        return max(self.numero1, self.numero2, self.numero3)
     #Numero Menor
    def menor(self):
        return min(self.numero1, self.numero2, self.numero3)
    #Verificar Igualdad
    def iguales(self):
        return self.numero1 == self.numero2 == self.numero3
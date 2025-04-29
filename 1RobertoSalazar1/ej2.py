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
    #Concatenar
    def concatenar(self):
        return str(self.numero1) + str(self.numero2) + str(self.numero3)   
         
n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
n3 = int(input("Numero 3: "))
numeros = Numeros(n1, n2, n3)

print("LA SUMA ES:", numeros.sumar())
print("EL NÚMERO MAYOR ES:", numeros.mayor())
print("EL NÚMERO MENOR ES:", numeros.menor())
print("¿TODOS SON IGUALES?:", numeros.iguales())
print("NÚMEROS CONCATENADOS:", numeros.concatenar())
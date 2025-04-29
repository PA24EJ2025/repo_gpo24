class Mi_clase:
    def __init__(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def sumar(self):
        return self.num1 + self.num2 + self.num3
    
    def mayor(self):
        return max(self.num1, self.num2, self.num3)
    
    def menor(self):
        return min(self.num1, self.num2, self.num3)
    
    def iguales(self):
        return self.num1 == self.num2 == self.num3
    
    def concatenar(self):
        return str(self.num1) + str(self.num2) + str(self.num3)
    
num1 = int(input("Ingresa el primer valor: "))
num2 = int(input("Ingresa el segundo valor: "))
num3 = int(input("Ingresa el tercer valor: "))

numeros = Mi_clase(num1,num2,num3)

print("La suma es: ",numeros.sumar())
print("El numero mayor es: ",numeros.mayor())
print("El numero menor es: ",numeros.menor())
print("Numeros iguales: ",numeros.iguales())
print("Numeros concatenados: ",numeros.concatenar())
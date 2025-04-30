class Mi_clase:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def Sumar(self):
        return self.num1 + self.num2 + self.num3

    def Mayor(self):
        mayor = self.num1
        if self.num2 > mayor:
            mayor = self.num2
        if self.num3 > mayor:
            mayor = self.num3
        return mayor

    def Menor(self):
        menor = self.num1
        if self.num2 < menor:
            menor = self.num2
        if self.num3 < menor:
            menor = self.num3
        return menor

    def Iguales(self):
        if self.num1 == self.num2 and self.num2 == self.num3:
            return True
        else:
            return False

    def Concatenar(self):
        return str(self.num1) + str(self.num2) + str(self.num3)
    
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
n3 = int(input("Ingresa el tercer número: "))

x = Mi_clase(n1, n2, n3)
print("La suma de los numeros ingresados es:", x.Sumar())
print("El mayor de los numeros ingresados es:", x.Mayor())
print("El menor de los numeros ingresados es :", x.Menor())
print("¿Iguales?:", x.Iguales())
print("Concatenado:", x.Concatenar())
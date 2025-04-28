class mi_clase:
    def __init__(self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def sumar(self):
        return (self.num1 + self.num2 + self.num3)

    def mayor(self):
        mayor = self.num1
        if self.num2 > mayor:
            mayor = self.num2

        if self.num3 > mayor:
            mayor = self.num3
        return mayor
    
    def menor(self):
        menor = self.num1
        if self.num2 < menor:
            menor = self.num2
        if self.num3 < menor:
            menor = self.num3
        return menor

    def iguales(self):
        return  (self.num1 == self.num2 == self.num3)
    

    def cocatenar(self):
        return str(self.num1)+str(self.num2)+str(self.num3)

n1 = int(input("ingresa el primer numero: "))
n2 = int(input("ingresa el segundo numero: "))
n3 = int(input("ingresa el tercer numero: "))

clase = mi_clase(n1,n2,n3)

print(f"la suma es {clase.sumar()}")
print(f"el numero mayor es: {clase.mayor()}")
print(f"el numero menor es: {clase.menor()}")
print(f"el numero es igual: {clase.iguales()}")
print(f"cocatenar {clase.cocatenar()}")
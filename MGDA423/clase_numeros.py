class Mi_clase:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def sumar(self):
        return self.num1 + self.num2 + self.num3
    def mayor(self):
        return max(self.num1,self.num2,self.num3)
    def menor(self):
        return min(self.num1,self.num2,self.num3)
    def iguales(self):
        return self.num1 == self.num2 == self.num3
    def concatenar(self):
        return f"{self.num1}{self.num2}{self.num3}"
         
mis_numeros = Mi_clase(13,4,9)

print("sumar",mis_numeros.sumar())
print("mayor", mis_numeros.mayor())
print("menor", mis_numeros.menor())
print("iguales", mis_numeros.iguales())
print("concatenar", mis_numeros.concatenar())
        
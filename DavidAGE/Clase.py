class mi_clase:
    def __init__(self, Num1, Num2, Num3):
        self.Num1 = num1
        self.Num2 = num2
        self.Num3 = num3

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
    
Numero = mi_clase(29, 10, 19)
print(f "Suma: ",(Numero.sumar))
print(f "Mayor: ",(Numero.mayor))
print(f "Menor: ",(Numero.menor))
print(f "Seran iguales?:  ",(Numero.iguales))
print(f "Concatenados": ,(Numero.concatenar))
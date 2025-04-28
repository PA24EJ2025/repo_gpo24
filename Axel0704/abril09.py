class Mi_clase:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    
    def Suma(self):
        return self.num1 + self.num2 + self.num3
    
    def nummayor(self):
        return max(self.num1, self.num2, self.num3)
    
    def nummenor(self):
        return min(self.num1, self.num2, self.num3)
    
    def numiguales(self):
        return self.num1 == self.num2 == self.num3
    
    def conca(self):
        return (f"Numeros: {self.num1}, {self.num2}, {self.num3}")


operacion = Mi_clase(5, 10, 5)
    
    
print("Suma:", operacion.Suma())           
print("el numero máximo es:", operacion.nummayor())        
print("el numero mínimo es:", operacion.nummenor())        
print("¿Los numeros son iguales?:", operacion.numiguales())
print(operacion.conca())              
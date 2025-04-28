class Mi_clase:
    def __init__(self, num1, num2, num3):
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

# Crear un objeto de la clase con valores de prueba
obj = Mi_clase(5, 5, 5)

# Llamar a los métodos y mostrar resultados
print("Suma:", obj.sumar())
print("Mayor:", obj.mayor())
print("Menor:", obj.menor())
print("¿Son iguales?:", obj.iguales())
print("Concatenado:", obj.concatenar())

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


# Aquí va la lógica principal del programa (fuera de la clase)
numero1 = int(input("Ingresa el número 1: "))
numero2 = int(input("Ingresa el número 2: "))
numero3 = int(input("Ingresa el número 3: "))

numero = Mi_clase(numero1, numero2, numero3)

print("Suma:", numero.sumar())
print("Mayor:", numero.mayor())
print("Menor:", numero.menor())
print("¿Son iguales?:", numero.iguales())
print("Concatenación:", numero.concatenar())
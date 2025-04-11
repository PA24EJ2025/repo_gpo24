class Mi_Clase:
    def _init_(self):
        self.num1 = float(input("Ingresa el primer número: "))
        self.num2 = float(input("Ingresa el segundo número: "))
        self.num3 = float(input("Ingresa el tercer número: "))
    def sumar(self):
        return self.num1 + self.num2 + self.num3
    def mostrar_mayor(self):
        return max(self.num1, self.num2, self.num3)
    def mostrar_menor(self):
        return min(self.num1, self.num2, self.num3)
    def mostrar_iguales(self):
        iguales = []
        if self.num1 == self.num2:
            iguales.append(self.num1)
        if self.num1 == self.num3:
            iguales.append(self.num1)
        if self.num2 == self.num3:
            iguales.append(self.num2)
        return iguales if iguales else "No hay números iguales"
    def concatenar(self):
        return str(self.num1) + str(self.num2) + str(self.num3)

mi_objeto = Mi_Clase()
print(f"La suma de los tres números es: {mi_objeto.sumar()}")
print(f"El número mayor es: {mi_objeto.mostrar_mayor()}")
print(f"El número menor es: {mi_objeto.mostrar_menor()}")
print(f"Los números iguales son: {mi_objeto.mostrar_iguales()}")
print(f"La concatenación de los números es: {mi_objeto.concatenar()}")
class Num1:
    def __init__(self, valor):
        self.valor = valor
    def sumar(self, n2, n3):
        return self.valor + n2.valor + n3.valor

    def mayor(self, n2, n3):
        return max(self.valor, n2.valor, n3.valor)

    def menor(self, n2, n3):
        return min(self.valor, n2.valor, n3.valor)

    def iguales(self, n2, n3):
        return self.valor == n2.valor == n3.valor

    def concatenar(self, n2, n3):
        return str(self.valor) + str(n2.valor) + str(n3.valor)
    

class Num2:
    def __init__(self, valor):
        self.valor = valor
    def sumar(self, n2, n3):
        return self.valor + n2.valor + n3.valor

    def mayor(self, n2, n3):
        return max(self.valor, n2.valor, n3.valor)

    def menor(self, n2, n3):
        return min(self.valor, n2.valor, n3.valor)

    def iguales(self, n2, n3):
        return self.valor == n2.valor == n3.valor

    def concatenar(self, n2, n3):
        return str(self.valor) + str(n2.valor) + str(n3.valor)


class Num3:
    def __init__(self, valor):
        self.valor = valor
    def sumar(self, n2, n3):
        return self.valor + n2.valor + n3.valor

    def mayor(self, n2, n3):
        return max(self.valor, n2.valor, n3.valor)

    def menor(self, n2, n3):
        return min(self.valor, n2.valor, n3.valor)

    def iguales(self, n2, n3):
        return self.valor == n2.valor == n3.valor

    def concatenar(self, n2, n3):
        return str(self.valor) + str(n2.valor) + str(n3.valor)

def obtener_numero(nombre):
    while True:
        try:
            return int(input(f"Introduce el valor de {nombre}: "))
        except ValueError:
            print("Ingresa otro valor: ")

valor1 = obtener_numero("Num1")
valor2 = obtener_numero("Num2")
valor3 = obtener_numero("Num3")

n1 = Num1(valor1)
n2 = Num2(valor2)
n3 = Num3(valor3)

print("Suma:", n1.sumar(n2, n3))             
print("Mayor:", n1.mayor(n2, n3))            
print("Menor:", n1.menor(n2, n3))            
print("¿Iguales?:", n1.iguales(n2, n3))      
print("Concatenar:", n1.concatenar(n2, n3)) 
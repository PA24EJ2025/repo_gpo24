class Mi_clase:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def sumar (self):
        return self.num1 + self.num2 + self.num3
    
    def mayor (self):
        return max(self.num1 ,self.num2 , self.num3)
    
    def menor (self):
        return min(self.num1 ,self.num2 , self.num3)
    
    def iguales (self):
        return self.num1 == self.num2 ==self.num3
    
    def concatenar (self):
        return str(self.num1) + str(self.num2) + str(self.num3)
    
nnum1 =int(input("ingresa el numero 1:  "))
nnum2 =int(input("ingresa el numero 2:  "))
nnum3 =int(input("ingresa el numero 3:  "))

nums= Mi_clase(nnum1,nnum2, nnum3)


print("LA SUMA ES: ", Mi_clase.sumar(nums))
print("EL NUMERO MAYOR ES: ", Mi_clase.mayor(nums))
print("EL NUMERO MENOR ES: ", Mi_clase.menor(nums))
print("¿IGUALES?: ", Mi_clase.iguales(nums))
print("LOS NUMEROS CONCATENADOS: ", Mi_clase.concatenar(nums))
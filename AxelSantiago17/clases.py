class Mi_clase:
    def __init__ (self,num1,num2,num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

def suma (self):
    return (self.num1+self.num2+self.num3)
def mayor(self):
    return max(self.num1,self.num2,self.num3)
def menor(self):
    return min(self.num1,self.num2,self.num3)
def iguales(self):
    return(self.num1 == self.num2 == self.num3)
def concatenar(self):
    return str(self.num1) + str(self.num2) + str(self.num3)


numero= Mi_clase(60,20,12)
print("suma:", numero.sumar())
print("mayor:", numero.mayor())
print("menor:", numero.menor())
print("iguales:", numero.iguales())
print("concatenos:", numero.concatenar())
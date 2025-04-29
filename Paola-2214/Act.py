class Mi_clase:
    def __init__(self, n1,n2,n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def sumar (self):
        sum= self.n1 + self.n2 + self.n3
        return sum
    def mayor (self):
        return max (self.n1,self.n2,self.n3)
    
    def menor (self):
        return min (self.n1,self.n2,self.n3)
    
    def iguales (self):
        if self.n1 == self.n2 == self.n3:
            return True
        else:
            return False
        
    def concatenar (self):
        return str(self.n1)+str(self.n2)+str(self.n3)
    
numero = Mi_clase(2,2,2)
print ("la suma es: ",numero.sumar())
print ("numm mayor: ",numero.mayor())
print ("num menor: ",numero.menor())
print ("¿los numeros son iguales?:",numero.iguales)
print ("num concatenados",numero.concatenar)
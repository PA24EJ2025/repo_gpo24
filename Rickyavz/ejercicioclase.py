class Mi_clase():
    def __init__(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
   
    def sumar(self):
        suma= (self.num1+self.num2+self.num3)
        return suma
    def mayor(self):
        return max(self.num1,self.num2,self.num3)
    
    def menor(self):
        return min(self.num1,self.num2,self.num3)
       
    def iguales(self):
         if (self.num1==self.num2==self.num3):
          print("Los numeros son iguales")
         else:
          print("No son iguales")
       
    def concatenar(self):
        return str(self.num1) + str(self.num2) + str(self.num3)
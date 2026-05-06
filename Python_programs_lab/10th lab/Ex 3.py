#Exercise 3
import math
class aritmethics:
    def __init__(self,a,b): # Конструктор на класа
        self.a=a
        self.b=b

    def sum(self):
        return self.a + self.b

    def dif(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b
 
    def rem(self):
        if(self.a != 0 and self.b != 0):
            return self.a / self.b
        else:
            print("Error!!!")
        
def add():
    x=float(input("a = "))
    y=float(input("b = "))
    T = aritmethics(x, y)
    return T

def input(list1):
    print("Input numbers: ")
    T = add
    list1.append(T)
    return list1

def output(list1):
    if list1 != []:
        for i in range(0, len(list1)):
            res_sum = list1[i].sum()
            #res_dif = list1[i].dif()
            #res_mult = list1[i].mult()
            #res_rem = list1[i].rem()
            print(f"Sum = {res_sum}")#;\nDif = {res_dif};\nMult = {res_mult};\nRem = {res_rem}")
    else:
        print("Empty!")

list = []
print(input.__doc__)
list = input(list)
print(output.__doc__)
output(list)
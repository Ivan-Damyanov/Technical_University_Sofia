#Exercise 1
import math
class Number: #Class
    def __init__(self,a): #Constructor of class
        self.a=a
    def show(self): #Methods
        return self.a
    def double(self):
        return math.pow(self.a,2)
    def triple(self): 
        return math.pow(self.a,3)
    def factorial(self):
        return math.factorial(self.a)
    
x=int(input("Въведете цяло число: ")) 

N=Number(x) 
print(f"a = {N.show()}") 
print(f"{x} ^ 2 = {int(N.double())}")
print(f"{x} ^ 3 = {int(N.triple())}")
print(f"{x}! = {int(N.factorial())}")

#N == self (self is the object which is created
#to which the methods are put)

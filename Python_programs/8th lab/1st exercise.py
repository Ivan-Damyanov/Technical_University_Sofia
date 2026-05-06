#Exercise 1
import math 
def calc1(x,y,z):
    P = x + y + z
    p=(x+y+z)/2
    s=math.sqrt(p*(p-x)*(p-y)*(p-z))
    return s

def calc2(x,y,z):
    P = x + y + z
    return P

a=float(input("a= "))
b=float(input("b= ")) 
c=float(input("c= "))

if (a+b<=c) or (a+c<=b) or (b+c<=a): 
    print("Не съществува такъв триъгълник!")
else:
    res_S = calc1(a,b,c)
    res_P = calc2(a,b,c)
    s = "%.2f"% (res_S)
    P = "%.2f"% (res_P)
    print(f"S = {s}")
    print(f"P = {P}")

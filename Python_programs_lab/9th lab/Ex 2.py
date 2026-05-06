#Exercise 2
import math
def calc(x=3,y=4,z=5): # Функция с три параметъра
    '''Изчислява лице на триъгълник'''
    if (x+y<=z) or (x+z<=y) or (y+z<=x): # Проверка за действителен триъгълник
        print("Не съществува такъв триъгълник!")
        return 0
    else:
        p=(x+y+z)/2
        s=math.sqrt(p*(p-x)*(p-y)*(p-z)) # Изчисляване на лицето на триъгълника
        return s
a=float(input("a= ")) # Въвеждане на първа страна на триъгълника
b=float(input("b= ")) # Въвеждане на втора страна на триъгълника
c=float(input("c= ")) # Въвеждане на трета страна на триъгълника
print(calc.__doc__)
print("Използване само на втората въведена страна")
rez=calc(y = b) 
if rez!=0:
    s="%.2f"% (rez)
    print(f"S = {s}")
    
print("Използване само на третата страна")
rez=calc(z = c) 
if rez!=0:
    s="%.2f"% (rez)
    print(f"S = {s}")
print("Използване само на втората и третата страна")
rez=calc(y = b, z = c)

if rez!=0:
    s="%.2f"% (rez)
    print(f"S = {s}")
print("Използване подразбиращите се стойности")
rez=calc() # x=3, y=4, z=5
if rez!=0:
    s="%.2f"% (rez)
    print(f"S = {s}")

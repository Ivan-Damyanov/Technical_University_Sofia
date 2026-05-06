#Exercise 2
import math 
import time 

total=[]
sum=0 
counter = 0

print("Въведете информация за избраните стоки")
print("Въведете код на стока 00 за край на въвеждането")

def format_stoka (x, y, z): 
    """Формира описание на една стока"""
    s="%.2f"% (y*z) 
    line="{x} ... X {z} ... {s} лв.".format(x=x,z=z,s=s)
    return line 
def resto(y,x): 
    return y-x
while True: 
    cod=input("\nВъведете код на стока: ")
    if cod=="00":
        break
    cena=float(input("Въведете цена на стока: ")) 
    broi=int(input("Въведете брой стоки: "))
    
    total.append(format_stoka(cod,cena,broi))
    sum+=cena*broi 
    counter += broi

print()
print("КАСОВА БЕЛЕЖКА:".center(35))
print("="*35)
for i in range(0,len(total)): # Извеждане на редовете на касовата бележка
    print(total[i].rjust(35))
s="%.2f"% (sum)
s1="ОБЩА СУМА: ..... {s} лв.".format(s=s)
s2 = "OБЩ БРОЙ ПРОДУКТИ: ..... X{counter}".format(counter=counter)
print(s1.rjust(35))
print(s2.rjust(35))
print(time.strftime("%d.%m.%Y %H:%M:%S").rjust(35)) # Извеждане на дата и време
print("="*35)
print()
r=float(input("Въведете предоставената сума пари: "))
ost=resto(r,sum) # Определяне на нужното ресто
if ost!=0:
    if ost>0:
        s="%.2f"% (ost)
        print(f"Ресто: {s} лв.")
    else:
        print("Сумата не е достатъчна!")
        s="%.2f"% math.fabs(ost)
        print(f"Не достигат {s} лв.")
else:
    print("Точна сума. Няма ресто!")

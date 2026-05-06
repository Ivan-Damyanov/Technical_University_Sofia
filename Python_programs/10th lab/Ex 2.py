#Exercise 2
import math
class Triangle: # Описание на клас Triangle
    fig_type="Triangles"
    def __init__(self,a,b,c): # Конструктор на класа
        self.a=a
        self.b=b
        self.c=c

    def show(self): # Метод за извеждане на страните на триъгълника
        s_a="%.2f"% (self.a)
        s_b="%.2f"% (self.b)
        s_c="%.2f"% (self.c)
        return f"a={s_a} cm, b={s_b} cm, c={s_c} cm"
    
    def lice(self): # Метод за изчисляване на лице
        p=(self.a+self.b+self.c)/2
        s=math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
        return s
    
    def perimetar(self): # Метод за изчисляване на периметър
        p = self.a+self.b+self.c
        return p
    
def add_triangle(): # Функция за добавяне на триъгълник
    while True:
        x=float(input("a, cm = "))
        y=float(input("b, cm = "))
        z=float(input("c, cm = "))
        if (x+y<=z) or (x+z<=y) or (y+z<=x): # Проверка за действителен триъгълник
            print("Не съществува такъв триъгълник!")
        else:
            T=Triangle(x,y,z) # Създаване на обекти от клас Triangle
            break
    return T

def inputdata(tr_list): # Функция за въвеждане на данните
    print("Колко триъгълника ще въведете?")
    count=int(input(">> "))
    for i in range(0,count):
        T=add_triangle()
        print()
        tr_list.append(T)
    return tr_list

def outputdata(tr_list): # Функция за извеждане на данните
    if tr_list!=[]:
        print(Triangle.fig_type)
        for i in range(0,len(tr_list)):
            print(tr_list[i].show())
    else:
        print("Списъкът е празен!")
        
def calc_lice(tr_list): # Функция за изчисляване на лице на триъгълник
    sum_f = 0
    if tr_list!=[]:
        for i in range(0,len(tr_list)):
            rez=tr_list[i].lice()
            s="%.2f"% (rez)
            sum_f += rez
            print(f"S = {s} cm2")
        print(f"Сбор на всички лица: {sum_f}")

    else:
        print("Списъкът е празен!")
        
def calc_perimetar(tr_list): # Функция за изчисляване на периметър на триъгълник
    sum_p = 0
    if tr_list!=[]:
        for i in range(0,len(tr_list)):
            rez=tr_list[i].perimetar()
            s="%.2f"% (rez)
            sum_p += rez
            print(f"P = {s} cm")
        print(f"Сбор на всички периметри: {sum_p}")
    else:
        print("Списъкът е празен!")
            
tr=[]
print(inputdata.__doc__)
tr=inputdata(tr)
print(outputdata.__doc__)
outputdata(tr)
print(calc_lice.__doc__)
calc_lice(tr)
print(calc_perimetar.__doc__)
calc_perimetar(tr)


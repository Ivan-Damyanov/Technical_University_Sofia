class Person: # Родителски клас
    ''' Клас за описание на човек'''
    firm_name="ABC Corporation"
    def __init__(self,name,age,salary): # Конструктор на родителски клас
        self.name=name
        self.age=age
        self.salary=salary
    def show_person(self): # Методи на родителски клас
        return f"{self.name} е на {self.age} години с {self.salary} лв. заплата"
    def get_name(self):
        return self.name
    def get_salary(self):
        return self.salary
    def get_age(self):
        return self.age

class PersonAll(Person): # Клас наследник
    '''Клас наследник'''
    def __init__(self,pos,name,age,salary): # Конструктор на класа наследник
        self.pos=pos
        super().__init__(name,age,salary) # Извикване на конструктор на родителския клас
    def show_personAll(self):
        return f"{self.name} е на {self.age} години с {self.salary} лв. заплата е на позиция {self.pos}"

def control_int():
    '''Контрол на входните данни'''
    while True:
        try: # Обработка на изключение
            num=int(input(">> "))
            return num
        except ValueError:
            print(control_int.__doc__)
            print("Необходимо е да се въведе цяло число!")
def control_float():
    '''Контрол на входните данни'''
    while True:
        try: # Обработка на изключение
            num=float(input(">> "))
            return num
        except ValueError:
            print(control_float.__doc__)
            print("Необходимо е да се въведе реално число!")
def add_person():
    '''Добавяне на човек в списъка'''
    x=input("Име: ")
    print("Възраст: ")
    y=control_int()
    print("Заплата: ")
    z=control_float()
    k=input("Позиция:")
    P=PersonAll(k,x,y,z) # Създаване на обекти от клас PersonAll
    return P
def inputdata(my_list): # Функция за въвеждане на група хора
    '''Въвеждане на данните'''
    print("Колко човека ще въведете?")
    count=control_int()
    for i in range(0,count):
        P=add_person()
        my_list.append(P)
    return my_list
def add_one(my_list): # Функция за добавяне на един човек
    '''Добавяне на един човек'''
    P=add_person()
    my_list.append(P)
    return my_list
def del_one(my_list): # Функция за изтриване на един човек
    '''Изтриване на един човек'''
    key=input("Въведете името на човека за изтриване:")
    flag=False
    for i in range(0,len(my_list)):
        if my_list[i].get_name()==key:
            del my_list[i]
            flag=True
            print("Един човек е изтрит")
            break
    if flag==False:
        print(f"Не е намерен човек с име {key} в списъка")
    return my_list
def outputdata(my_list): # Функция за извеждане на основни данни
    '''Извеждане на основни данни'''
    if my_list!=[]:
        print(Person.firm_name)
        for i in range(0,len(my_list)):
            print(my_list[i].show_person())
    else:
        print("Списъкът е празен!")
def outputdataAll(my_list): # Функция за извеждане на всички данни
    '''Извеждане на данните с позиции'''
    if my_list!=[]:
        print(Person.firm_name)
        for i in range(0,len(my_list)):
            print(my_list[i].show_personAll())
    else:
        print("Списъкът е празен!")
def max_salary(my_list): # Функция за определяне на човека с най-високата заплата
    '''Определяне на човека с най-висока заплата'''
    if my_list!=[]:
        m=my_list[0].get_salary()
        index=0
        for i in range(1,len(my_list)):
            if my_list[i].get_salary()>m:
                m=my_list[i].get_salary()
                index=i
        print("Човекът с най-висока заплата е:")
        print(my_list[index].show_person())
    else:
        print("Списъкът е празен!")
def min_age(my_list): # Функция за намиране на най-младия човек
    '''Намиране на най-младия човек'''
    if my_list!=[]:
        m=my_list[0].get_age()
        index=0
        for i in range(1,len(my_list)):
            if my_list[i].get_age()<m:
                m=my_list[i].get_age()
                index=i
        print("Най-младият човек е:")
        print(my_list[index].show_person())
    else:
        print("Списъкът е празен!")

def salary_30(my_list):
    '''Изчисляване на средна заплата на хора под 30 години'''
    if my_list != []:
        average_sal = 0
        counter = 0
        for i in range(0, len(my_list)):
            if my_list[i].get_age() < 30:
                average_sal += my_list[i].get_salary()
                counter += 1
        if average_sal > 0 and counter > 0:
            average_sal = average_sal/counter
            print(f"The average salary for people below 30 years is: {average_sal}")
        else:
            print("There are no employees below 30 years of age.")
    else:
        print("The list is empty!")

def del_all(my_list): # Функция за изтриване на списъка
    '''Изтриване на целия списък'''
    my_list.clear()
    print("Всички хора от списъка са изтрити!")
    return my_list
def sort_list(my_list): # Функция за сортиране на списъка
    '''Сортиране на списъка'''
    tmp=Person("",0,0)
    for i in range(0,len(my_list)-1): # Сортиране по метода на мехурчето
        for j in range(i+1,len(my_list)):
            if my_list[i].get_name()>my_list[j].get_name():
                tmp=my_list[i]
                my_list[i]=my_list[j]
                my_list[j]=tmp
    print("Списъкът е сортиран по имената на хората")

lst=[] # Създаване на празен списък
responce=1
while responce:
    print('''Изберете команда
        1 - Въвеждане на начални данни
        2 - Добавяне на един човек
        3 - Извеждане на основни данните
        4 - Намиране на човека с най-висока заплата
        5 - Намиране на най-младия човек
        6 - Изтриване на един човек
        7 - Изтриване на целия списък
        8 - Сортиране по име
        9 - Извеждане на заеманите позиции
        10 - Изчисляване на средна заплата на хора под 30 години
        11 - Изход''')
    print("Код: ")
    responce=control_int()
    if responce==1:
        print(inputdata.__doc__)
        lst=inputdata(lst) # Обектите се записват в списък, който се подава като параметър
    elif responce==2:
        print(add_one.__doc__)
        add_one(lst)
    elif responce==3:
        print(outputdata.__doc__)
        outputdata(lst)
    elif responce==4:
        print(max_salary.__doc__)
        max_salary(lst)
    elif responce==5:
        print(min_age.__doc__)
        min_age(lst)
    elif responce==6:
        print(del_one.__doc__)
        lst=del_one(lst)
    elif responce==7:
        print(del_all.__doc__)
        lst=del_all(lst)
    elif responce==8:
        print(sort_list.__doc__)
        sort_list(lst)
    elif responce==9:
        print(outputdataAll.__doc__)
        outputdataAll(lst)
    elif responce == 10:
        print(salary_30.__doc__)
        salary_30(lst)
    else:
        print("Довиждане!")
        responce=0
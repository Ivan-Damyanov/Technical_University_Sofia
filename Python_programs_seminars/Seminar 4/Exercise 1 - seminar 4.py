def area_square(x): # Функция за изчисляване на лице на квадрат
    '''Изчислява лице на квадрат'''
    return x*x
def area_rect(x,y): # Функция за изчисляване на лице на правоъгълник
    '''Изчислява лице на правоъгълник'''
    return x*y
def area_trian(x,y): # Функция за изчисляване на лице на триъгълник
    '''Изчислява лице на триъгълник'''
    return x*y/2
def area_sirc(x): # Функция за изчисляване на лице на кръг
    '''Изчислява лице на кръг'''
    return 3.14*x*x
def area_tra(x,y,z): # Функция за изчисляване на лице на равнобедрен трапец
    '''Изчислява лице на равнобедрен трапец'''
    return (x+y)*0.5*z
def perimeter(choice,x,y,z):
    if choice == 1:
        return 2*x
    elif choice == 2:
        return x + y
    elif choice == 3:
        return x + y + z
    elif choice == 4:
        return 2*3.14*x
    elif choice == 5:
        return 2*x + 2*y
responce=1
while responce:
    print('''Select comand
        1 - Лице на квадрат
        2 - Лице на правоъгълник
        3 - Лице на триъгълник
        4 - Лице на кръг
        5 - Лице на равнобедрен трапец
        6 - Периметър на геометрична фигура
        7 - Изход''')
    responce=int(input(">> "))
    if responce==1:
        a=float(input("страна = "))
        print(area_square.__doc__)
        print("S = %.2f " % area_square(a)) # Викане на функция area_square()
    elif responce==2:
        a=float(input("широчина = "))
        b=float(input("широчина = "))
        print(area_rect.__doc__)
        print("S = %.2f " % area_rect(a,b)) # Викане на функция area_rect()
    elif responce==3:
        a=float(input("страна = "))
        b=float(input("височина = "))
        print(area_trian.__doc__)
        print("S = %.2f" % area_trian(a,b)) # Викане на функция area_trian()
    elif responce==4:
        a=float(input("радиус = "))
        print(area_sirc.__doc__)
        print("S = %.2f" % area_sirc(a)) # Викане на функция area_sirc()
    elif responce==5:
        a=float(input("малка основа = "))
        b=float(input("голяма основа = "))
        h=float(input("височина = "))
        print(area_tra.__doc__)
        print("S = %.2f" % area_tra(a,b,h)) # Викане на функция area_tra()
    elif responce == 6:
        print('''Select comand
            1 - Kвадрат
            2 - Pравоъгълник
            3 - Tриъгълник
            4 - Kръг
            5 - Rавнобедрен трапец''')
        figure_per = 1
        while figure_per:
            figure_per = int(input("Изберете фигура, чиято обиколка да се изчисли: "))
            if figure_per == 1:
                a=float(input("страна = "))
                b = 0
                c = 0
                print(perimeter.__doc__)
                print("P sq = %.2f" % perimeter(figure_per, a, b, c))
            elif figure_per == 2:
                a=float(input("широчина = "))
                b=float(input("широчина = "))
                c = 0
                print(perimeter.__doc__)
                print("P rec = %.2f" % perimeter(figure_per, a, b, c))
            elif figure_per == 3:
                a=float(input("страна = "))
                b=float(input("височина = "))
                c = 0
                print(perimeter.__doc__)
                print("P tr = %.2f" % perimeter(figure_per, a, b, c))
            elif figure_per == 4:
                a=float(input("радиус = "))
                b = 0
                c = 0
                print(perimeter.__doc__)
                print("P = %.2f" % perimeter(figure_per, a, b, c))
            elif figure_per == 5:
                a=float(input("малка основа = "))
                b=float(input("голяма основа = "))
                h=float(input("височина = "))
                print(perimeter.__doc__)
                print("P = %.2f" % perimeter(figure_per, a, b, h))
            else:
                figure_per = 0
    else:
        print("Довиждане!")
        responce = 0
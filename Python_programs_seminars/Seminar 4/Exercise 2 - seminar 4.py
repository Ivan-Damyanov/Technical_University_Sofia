def calc(x,y): # функция за извършване на изчисления
    '''Изчислява сума, разлика и произведение от две числа'''
    a=x+y
    b=x-y
    c=x*y
    return (a,b,c) # връщане на резултатите като кортеж
def mult(x,y):
    '''Удвоява първото и утроява второто число'''
    a = 2 * x
    b = 3 * y
    return(a,b)

first=float(input(">> "))
second=float(input(">> "))

print(calc.__doc__)
tup1=calc(first, second) # викане на функция func()
print(tup1)

print(mult.__doc__)
tup2 = mult(first, second)
print(tup2)
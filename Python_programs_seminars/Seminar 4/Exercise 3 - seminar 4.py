def func(*x): # функция с параметър кортеж
    '''Работи с кортеж като входен параметър'''
    result=0
    for i in x: # сумиране на числата от кортежа
        result+=i
    print(x)
    print(result)

def even(x):
    '''Сумира четните числа'''
    even_sum = 0
    for i in x:
        if i  % 2 == 0:
            even_sum += i
    print(x)
    print(even_sum)

a = tuple(map(int, input("Enter a multiple value: ").split()))

print(func.__doc__)
func(*a)

print(even.__doc__)
even(a)
#Exercise 2
counter = 0
i_even = 0

for i in range(0,10):
    num = int(input("num = "))

    if num % 2 == 0 and counter == 0:
        min = num
        counter = 1

    if num % 2 == 0 and counter == 1: 
        i_even += 1 
        if min > num:
            min = num

print(f"min = {min}") 
print(f"counter = {i_even}") 
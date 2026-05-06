#Exercise 3
counter = 0
i_even = 0

for i in range(0,10):
    num = int(input("num = "))

    if num % 2 != 0 and counter == 0:
        max = num
        counter += 1

    if num % 2 != 0 and counter == 1: 
        i_even += 1 
        if num > max:
            max = num 

print(f"max = {max}") 
print(f"counter = {i_even}") 
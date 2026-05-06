#1st exercise
x = int(input("x = "))
if x % 2 == 0:
    print(f"{x} is even number")
else:
    print(f"{x} is odd number")

#2nd exercise
y = int(input("y = "))

if y == 1:
    print(f"{y} = Monday")
elif y == 2:
    print(f"{y} = Tuesday")
elif y == 3:
    print(f"{y} = Wednesday")
elif y == 4:
    print(f"{y} = Thursday")
elif y == 5:
    print(f"{y} = Friday")
elif y == 6:
    print(f"{y} = Saturday")
elif y == 7:
    print(f"{y} = Sunday")
else:
    print(f"{y} = IMPOSSIBLE!!!")

#3rd exercise
z = int(input("z = "))

if z < 1 or z > 10:
    print(f"{z} doesn't belong to the interval [1;10]")
    if z < 1:
        print(f"{z} is less than 1")
        print("End of program")
    else:
        print(f"{z} is more than 10")
        print("End of program")
    
else:
    print(f"{z} belongs to the interval [1;10]")
    print("End of program")

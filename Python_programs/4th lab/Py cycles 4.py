#Exercise 4

c = 0
limit = int(input("How many numbers do you want to grade:"))

for i in range (0, limit):
    a = int(input("a = "))
    b = int(input("grade of a = "))
    c = a ** b
    print(f"{c} = {a} ** {b}")
    print(f"{b} grade of {a} = {c}")
    

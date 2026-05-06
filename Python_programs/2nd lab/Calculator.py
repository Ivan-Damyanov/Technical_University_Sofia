#4th exercise
#Calculator

a = float(input("First number = "))
b = float(input("Second number = "))
c = 0

print("Choose type of calc (its number):")
print("1 - '+'")
print("2 - '-'")
print("3 - '*'")
print("4 - '/'")

sign = int(input("Type: "))

if sign == 1:
    c = a + b
    print(f"{a} + {b} = {c}")
    print(f"{c} is the sum of your numbers.")
elif sign == 2:
    c = a - b
    print(f"{a} - {b} = {c}")
    print(f"{c} is the difference between your numbers.")
elif sign == 3:
    c = a * b
    print(f"{a} * {b} = {c}")
    print(f"{c} is the multiplication between your numbers.")
elif sign == 4:
    c = a / b
    print(f"{a} / {b} = {c}")
    print(f"{c} is the deivision between your numbers.")
    c = a % b
    print(f"{a} % {b} = {c}")
    print(f"{c} is the leftover after the point.")
else:
    print("I couldn't understand.")

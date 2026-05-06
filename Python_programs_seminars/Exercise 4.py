#Exercise 4
total_n = 0
in_bounds_n = 0
sum = 0
while True:

    min = int(input("Minimum num: "))
    max = int(input("Maximum num: "))
    if min < max:
        break
    else:
        print("Impossible limits!")

for i in range(0, 10):
    num = int(input("num = "))
    total_n += 1
    if num >= min and num <= max:
        in_bounds_n += 1
        sum += num

print(f"Total numbers: {total_n}")
print(f"Numbers in boundries: {in_bounds_n}")
print(f"Sum of all numbers in boundries: {sum}")
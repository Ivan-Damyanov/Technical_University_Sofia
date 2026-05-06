#Example 3
sum = 0
br = 0

while True:
    a = float(input("a = "))
    if a == -99:
        break
    if a < 0 and a % 2 == 0:
        br+=1
        continue
    if a > 0 and a % 2 == 0:
        br+=1
        continue
    sum += a
print(f"sum = {sum}")
print(f"There are {br} even numbers")


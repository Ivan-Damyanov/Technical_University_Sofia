#Exercise 1
evensum = 0
evencount = 0
oddsum = 0
oddcount = 0

for i in range(0, 10):
    num = int(input("num = "))
    if num % 2 == 0:
        evensum += num
        evencount += 1
    else:
        oddsum += num
        oddcount += 1

print(f"\nTotal sum of even numbers: {evensum}")
print(f"Total sum of odd numbers: {oddsum}\n")

evensum /= evencount
oddsum /= oddcount
print(f"Аrithmetic mean value of even numbers: {evensum}")
print(f"Arithmetic mean value of odd numbers: {oddsum}\n")
#Example 2
sum = 0
index = 0
while index < 10:
    a = int(input("a = "))
    sum += a
    index += 1
print(f"sum = {sum}")

sum = sum % 2
if sum == 0:
    print("Sum is even number.")
else:
    print("Sum is odd number.")

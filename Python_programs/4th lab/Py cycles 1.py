#Example 1
sum = 0

limit = int(input("Limit of sums = "))

for i in range(0,limit):
    a = float(input("a = "))
    sum += a
print(f"sum = {sum}")

print("sum = %f" % sum)

a = float(input("Enter a = "))
b = float(input("Enter b = "))

x = a

a += b
print(a)
print(type(a))

a = x

a -= b
print(a)
print(type(a))

a = x

a *= b
print(a)
print(type(a))

a = x

a /= b
print(a)
print(type(a))

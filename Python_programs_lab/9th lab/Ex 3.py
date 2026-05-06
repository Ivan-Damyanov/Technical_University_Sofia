#Exercise 3
import math
def sum(x = 1, y = 1):
    s = x + y
    return s

def sub(x = 1, y = 1):
    sb = x - y
    return sb

def mult(x = 1, y = 1):
    m = x * y
    return m

a = int(input("Type first number: "))
b = int(input("Type second number: "))

print(sum.__doc__)
print("Sum with both nums: ")
res=sum(a, b)
if res!=0:
    s="%.2f"% (res)
    print(f"Sum = {s}")
print("Sum with first num: ")
res=sum(a)
if res!=0:
    s="%.2f"% (res)
    print(f"Sum = {s}")
print("Sum with second num: ")
res=sum(b)
if res!=0:
    s="%.2f"% (res)
    print(f"Sum = {s}")
print("Sum without any of those nums: ")
res=sum()
if res!=0:
    s="%.2f"% (res)
    print(f"Sum = {s}")

print(sub.__doc__)
print("Sub with both nums: ")
res=sub(a, b)
if res!=0:
    sb="%.2f"% (res)
    print(f"Sub = {sb}")
print("Sub with first num: ")
res=sub(a)
if res!=0:
    sb="%.2f"% (res)
    print(f"Sub = {sb}")
print("Sub with second num: ")
res=sub(b)
if res!=0:
    sb="%.2f"% (res)
    print(f"Sub = {sb}")
print("Sub without any of those nums: ")
res=sub()
if res!=0:
    sb="%.2f"% (res)
    print(f"Sub = {sb}")

print(mult.__doc__)
print("Mult with both nums: ")
res=mult(a, b)
if res!=0:
    m="%.2f"% (res)
    print(f"Mult = {m}")
print("Mult with first num: ")
res=mult(a)
if res!=0:
    m="%.2f"% (res)
    print(f"Mult = {m}")
print("Mult with second num: ")
res=mult(b)
if res!=0:
    m="%.2f"% (res)
    print(f"Mult = {m}")
print("Mult without any of those nums: ")
res=mult()
if res!=0:
    m="%.2f"% (res)
    print(f"Mult = {m}")

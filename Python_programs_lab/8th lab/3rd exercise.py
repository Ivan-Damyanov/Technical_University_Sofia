#Exercise 3
import math
def celcius(f):
    C = (f - 32) * 5/9
    return C

def farenhide(c):
    F = c * 9/5 + 32
    return F

c_temp = float(input("Temperature in celcius: "))
f_temp = float(input("Temperature in farenhide: "))

tempC = celcius(f_temp)
tempF = farenhide(c_temp)

C = "%.2f"%(tempC)
F = "%.2f"%(tempF)

print(f"Temperature in C: {C}")
print(f"Temperature in F: {F}")

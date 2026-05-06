#Exercise 1
from matplotlib import pyplot as plt
import numpy as np # Импортиране на numpy
Lx=[] # Създаване на празен списък
Ly=[] # Създаване на празен списък
print("Въведете целочислени координати за 10 точки:")
for i in range(0,10):
    while True: # Контрол на входните данни за x
        try:
            x=int(input("x>> "))
            Lx.append(x)
            break
        except ValueError:
            print("Въведете цяло число!")
    while True: # Контрол на входните данни за y
        try:
            y=int(input("y>> "))
            Ly.append(y)
            break
        except ValueError:
            print("Въведете цяло число!")

x_point = np.array(Lx)
y_point = np.array(Ly)
plt.plot(x_point,y_point,'y--o', label='points') # Изчертаване на графиката
plt.grid(axis = 'x', color = 'black', linestyle = ':', linewidth = '0.5')
plt.xlabel("X координати")
plt.ylabel("Y координати")
plt.title("Изобразяване на линейна графика")
plt.legend()
plt.savefig("upr14_image1.png")
plt.show()


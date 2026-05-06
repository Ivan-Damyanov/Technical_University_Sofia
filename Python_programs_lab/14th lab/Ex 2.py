#Exercise 2
import matplotlib.pyplot as plt # Импортиране на matplotlib
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
plt.scatter(x_point,y_point,color='blue',s=15, label='dots')
plt.xlabel("X координати")
plt.ylabel("Y координати")
plt.title("Изобразяване на линейна графика")
plt.savefig("upr14_image2.png")
plt.legend(loc = 'upper left')
plt.show()

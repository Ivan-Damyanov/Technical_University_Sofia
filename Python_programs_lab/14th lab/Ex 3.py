#Exercise 3
import matplotlib.pyplot as plt # Импортиране на matplotlib
import numpy as np # Импортиране на numpy
Lx=[] # Създаване на празен списък
Ly=[] # Създаване на празен списък
print("Въведете 10 категории и целочислени стойности:")
for i in range(0,10):
    x=input("категория: ") # Въвеждане на категории
    Lx.append(x)
    while True: # Контрол на входните данни за стойностите
        try:
            y=int(input("стойност: "))
            Ly.append(y)
            break
        except ValueError:
            print("Въведете цяло число!")
x_point = np.array(Lx)
y_point = np.array(Ly)
plt.barh(x_point,y_point,color='blue',height=0.3, label='bars')
plt.xlabel("Категории")
plt.ylabel("Стойности")
plt.title("Изобразяване на данни по категории")
plt.legend() # Показване на легенда
plt.savefig("upr14_image3.png")
plt.show()

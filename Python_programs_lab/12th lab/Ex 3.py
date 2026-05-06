#Exercise 3
suma=0
index=0
fc_name = input("Choose faculty(ftk, fett): ")
with open("data.txt","r",encoding="utf-8") as f: # Отваряне на файла за четене
    for s in f: # Обхождане на файла ред по ред
        ls=s.split(" ") # Запис на данните в списък
        print(f"{ls[0]} {ls[1]} {ls[2]} {ls[3]} {ls[4]}",end="")
        if ls[2] == fc_name:
            suma+=int(ls[1])
            index+=1
        
try:
    av = suma/index # Изчисляване на средната възраст на студентите
    r = "%.2f"%(av)
    print(f"\nThere are {index} students with av = {r} in faculty {fc_name}.")
except ZeroDivisionError:
    print(f"There are no students in faculty {fc_name}!")
#Exercise 1
with open("test.txt","w",encoding="utf-8") as f: # Отваряне на файла за запис
    for i in range(0,5):
        str=input(f"Низ {i+1}: ")
        f.write(f"{str}\n")
        
with open("test.txt","r",encoding="utf-8") as f: # Отваряне на файла за четене
    for i in range(0,5):
        print(f.readline(), end = "")

lst = []
with open("test.txt","r",encoding="utf-8") as f: # Отваряне на файла за четене
    for i in f:
        lst.append(i)
    print(lst)

#Exercise 2
s1=set() # Създаване на празно множество
s2=set() # Създаване на празно множество

print(type(s1))
print(type(s2))

num1 = int(input("Type how many elements you want in s1 set: "))
for i in range(0, num1):
    s=int(input("Елемент I множество: "))
    s1.add(s) # Добавяне на елемент
    #Може да се направи също и със len(s1) = n
    
print("I множество: ")
print(s1)

num2 = int(input("Type how many elements you want in s1 set: "))
for i in range(0,num2):
    s=int(input("Елемент II множество: "))
    s2.add(s) # Добавяне на елемент
    #Може да се направи също и със len(s2) = n

print("II множество: ")
print(s2)

s3=s1|s2
print("Обединение на множества I и II: ")
print(s3)

s3=s1-s2
print("Разлика на множества I и II: ")
print(s3)

s3=s1&s2
print("Пресичане на множества I и II: ")
print(s3)

s=int(input("Елемент, който да се премахне от I множество: "))

if s in s1:
    s1.remove(s) # Премахване на елемент от първо множество
else:
    print(f"{s} не се съдържа в множество I")
    
print(f"Set s1 before clearing: {s1}")
print("Изчистване на множество I:")
s1.clear() # Изчистване на множество
print(f"Set s1 after clearing: {s1}")

print(f"Set s1 before clearing: {s2}")
print("Изчистване на множество II:")
s2.clear() # Изчистване на множество
print(f"Set s1 after clearing: {s2}")

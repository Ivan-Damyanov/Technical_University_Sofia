city=["Sofia","Paris","London","Berlin","Madrid"] # Начален списък
responce=1
print("The current list is:")
print(city)
print("Count of elements is %d" % len(city))
while responce:
    print('''Select comand # Извежда меню
    1 - Add city
    2 - Remove city
    3 - Display list
    4 - Find a city
    5 - Sort cities
    6 - Create new list and merge both lists
    7 - Exit''')
    responce=int(input(">>"))
    if responce==1: # Добавяне на град
        key=input("City name: ")
        city.insert(len(city),key)
        print("Added!")
    elif responce==2: # Изтриване на град
        key=input("Del city name: ")
        if key in city:
            city.remove(key)
            print("Removed!")
        else:
            print("%s is not in the list!" % key)
    elif responce==3: # Отпечатване на списъка
        print(city)
    elif responce==4: # Търсене на град
        key=input("Find city name: ")
        if key in city:
            print("%s is in the list!" % key)
        else:
            print("%s is not in the list!" % key)
    elif responce==5: # Сортиране на списъка
        city.sort()
        print("Sorted!")
    elif responce == 6:
        city2_list = []
        num = int(input("Choose how many cities you wish to add to this new list: "))
        for i in range(0, num):
            element = input("Input city: ")
            city2_list.append(element)
        city_list = city + city2_list
        print(f"New list(from both lists): {city_list}")
    else: # Изход
        print("See you soon!")
        responce=0
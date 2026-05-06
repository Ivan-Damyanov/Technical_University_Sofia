dict={ # Начален речник
    "house":"къща",
    "egg":"яйце",
    "cat":"котка",
    "dog":"куче",
    "fish":"риба"}
print("Current dict is: ");
print("Dict includes %d words" % len(dict))
for word in dict:
    print(word,": ",dict[word])
print(''' Select command # Извежда меню
    1 - Add word
    2 - Delete a word
    3 - Display dict
    4 - Find a word
    5 - Sort dictionaries
    6 - Exit''')
responce=1
while responce:
    responce=int(input(">> "))
    if responce==1: # Добавя дума
        word = input("Enter the word: ")
        value = input("Enter translation: ")
        dict[word]=value
        print("Added!")
    elif responce==2: # Изтрива дума
        word = input("Enter the word: ")
        if word in dict:
            del dict[word]
            print("Deleted!")
        else:
            print("%s is not in the dict" % word)
    elif responce==3: # Извежда речника
        for word in dict:
            print(word,": ",dict[word])
    elif responce==4: # Търси дума
        word = input("Enter the word: ")
        if word in dict:
            print("%s is in the dict!" % word)
        else:
            print("%s is not in the dict!" % word)
    elif responce == 5:
        keys = list(dict.keys())
        keys.sort()
        for i in keys:
            print(i," : " ,dict[i])
    else: # Изход
        print("See you soon!")
        responce=0
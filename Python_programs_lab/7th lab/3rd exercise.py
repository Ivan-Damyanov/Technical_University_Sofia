#Exercise 3
dict={}
max = 0

for i in range(0,7):
    key=input("Key (str): ")
    val=int(input("Value (int): "))
    dict[key]=val

print("Overall content in dictionary:")
for key in dict.keys():
    print(key,": ", dict[key])

for key in dict.keys():
    if dict[key] > max:
        max = dict[key]
        key_max = key

print(f"Biggest number in dict: {max}")
print(f"Key of biggest number: {key_max}")

ch_key = input("Choose key to change its value: ")
ch_val = int(input("Type new value of chosen key: "))
if ch_key in dict:
    dict[ch_key] = ch_val
    print("New content in dictionary:")
    for key in dict.keys():
        print(key,": ", dict[key])
else:
    print("No such key!")

del_key = input("Choose which key to delete: ")
if del_key in dict:
    del dict[del_key]
    print(dict)
else:
    print("No such key!")

add_key = input("Type new key to be added to dict (str): ")
add_val = int(input("Type value of new key (int): "))
dict[add_key] = add_val
print(f"Dict with new key and value:\n{dict}")

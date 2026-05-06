#Exercise 1 - 11/10/2023
lst=[]

for i in range(0,5):
    x=int(input("x = "))
    lst=lst+[x,]
    
print(lst)

lst1=lst*2
print(f"Doubled list: {lst1}")

key=int(input("Searched element: "))

if key in lst: 
    print(f"{key} is in list")
else:
    print(f"{key} isn't in list")
for i in range(0,len(lst)):
    print(lst[i])
    
lst.sort() 
print(f"Sorted list: {lst}")

max_el=max(lst)
print(f"max = {max_el}")

index=int(input("Index of element to change: "))
val=int(input("New value of element: "))

if index<len(lst):
    lst[index]=val
    print(f"Changed element: {lst}")
else:
    print(f"No such index {index} in list")

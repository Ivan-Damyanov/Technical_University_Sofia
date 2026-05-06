#Exercise 2
lst=[]

for i in range(0,5):
    x=int(input("x = "))
    lst=lst+[x,]
    
print(lst)

index = int(input("Choose index element you want to delete: "))
del lst[index]

print(lst)

#Exercise 4
lst=[]

for i in range(0,7):
    x = input("x = ") #asd, asdasd, asf, w, dsr, afre, ars
    lst=lst+[x,]
    
print(lst)

max_el = "sth" #max
n = 0
m = 0

for i in range(0,len(lst)):
    n = 0
    for j in range(0,len(lst[i])):
        n += 1
        if(n > m):
            m = n
            max_el = lst[i]

print(f"Biggest string in tpl is {max_el}") #max

replace = int(input("Choose index of element to change its value: "))#replace
replacement = input("New value of chosen element: ")

elem = lst[replace]
elem = elem.replace(elem, replacement)
lst[replace] = elem 
print(lst)#replace

rem = int(input("Choose index of element to remove it from list: ")) #remove + insert
remrepl = input("Input value for new element for the same index in list: ")
del lst[rem]
lst.insert(rem, remrepl)
print(lst)#remove + insert

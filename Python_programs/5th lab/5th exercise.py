#Program 5
tpl = ()

for i in range(0, 7):
    str = input("str = ")
    tpl = tpl + (str,)

print(tpl)

max_el = "sth"
n = 0
m = 0

for i in range(0,len(tpl)):
    n = 0
    for j in range(0,len(tpl[i])):
        n += 1
        if(n > m):
            m = n
            max_el = tpl[i]
            
            

print(f"Biggest string in tpl is {max_el}")

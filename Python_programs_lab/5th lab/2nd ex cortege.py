#Exercise 2 - 11/10/2023
tpl = ()
for i in range(0, 5):
    x = int(input("x = "))
    tpl = tpl + (x,)

print(tpl)
tpl1 = tpl * 2
print(f"Doubled cortege: {tpl1}")

key = int(input("Searched element: "))
if key in tpl:
    print(f"{key} is in the cortege")
else:
    print(f"{key} isn't in the cortege")

for i in range(0,len(tpl)):
    print(tpl[i])
    
min_el = min(tpl)
print(f"min = {min_el}")

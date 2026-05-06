#Exercise 1 - 11/10/2023
str = input("Input a string: ")
str1 = str * 2
print(f"Doubled string: {str1}")

add = input("Input a second string: ")
str2 = str + add
print(f"Put strings together are: {str2}")

for i in range(0, len(str)):
    print(str[i])

fstr = input("Search a substring: ")
n = str.find(fstr)

if n!=-1:
    print(f"{fstr} is on {n} position in string {str}")
else:
    print(f"{fstr} doesn't belong to the string {str}")

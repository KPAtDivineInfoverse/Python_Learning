marks = [3,5,6,"Kip",True]
print(marks)
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

print(marks[-3]) #negative index
print(marks[len(marks)-3]) #positive index
print(marks[5-3]) #positive index
print(marks[2]) #positive index

if 6 in marks:
    print("Yes")
else:
    print("No")


if "6" in marks:
    print("Yes")
else:
    print("No")


if "Kip" in marks:
    print("Yes")
else:
    print("No")
    
#same thing for string
if "sh" in "Kapish":
    print("Yes")
else:
    print("No")
    
print(marks[:])
print(marks[2:4])
print(marks[0:5])
print(marks[0:5:2])
print(marks[0:5:3])

lst1=[i*i for i in range(10)]
print(lst1)
lst2=[i*i for i in range(10) if i%2==0]
print(lst2)
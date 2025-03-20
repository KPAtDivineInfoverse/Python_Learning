names="Kip,Dp"
print(names[0:3])

fruit="Mango"
len1=len(fruit)
print("Mango Is",len1,"Letter Word.")

print(fruit[0:4])
print(fruit[1:4])
print(fruit[:5])

#this two print statement works same
print(fruit[0:-3])
print(fruit[0:len(fruit)-3])

#this two print statement works same
print(fruit[len(fruit)-3:len(fruit)-1])
print(fruit[-3:-1])

alphabets="ABCDE"
for i in alphabets:
    print(i)

hr="harry"
print(hr[-4:-2])
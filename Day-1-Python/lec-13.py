a="Kip"
b="  Kapish  "
print(a.upper())
print(a.lower())
print(b)
print(b.strip())

c="!!kip!!"
print(c)
print(c.rstrip("!"))
print(a.replace("Kip","Kapish"))

d="Kapish Kp Dp"
print(d.split(" "))

heading="hello kip"
print(heading.capitalize())

str1="Welcome to python"
print(len(str1))
print(len(str1.center(50)))
print(str1.center(50))
print(str1.center(50,"."))

print(str1.count("o"))

str2="Kapish Panchal Kapish"
print(str2.count("Kapish"))
print(str2.endswith("Kapish"))
print(str2.endswith("sh"))
print(str1.endswith("to",4,10))

str3="He's name is Dan. He is an honest man."
print(str3.find("is"))
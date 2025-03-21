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
print(str3.index("Dan"))

str4="WelcomeToPython"
print(str4.isalnum())
str4="WelcomeToPython007"
print(str4.isalnum())
print(str4.isalpha())
str4="WelcomeToPython"
print(str4.isalpha())
print(str4.islower())
str4="welcometopython"
print(str4.islower())
print(str4.isprintable())
str4="welcometopython\n"
print(str4.isprintable())

str5="      " #using spacebar
print(str5.isspace())
str5="      " #using Tab
print(str5.isspace())
str5="Welcome To Python"
print(str5.isspace())
print(str5.istitle())
str5="Welcome to python"
print(str5.istitle())

str6="WORLD HEALTH ORGANIZATION"
print(str6.isupper())

str7="Python Is Good Language"
print(str7.startswith("Python"))
print(str7.swapcase())

str8="He's name is Dan"
print(str8.title())
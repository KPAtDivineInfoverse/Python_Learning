import os
os.system("python --version")

x=8

match x:
    case 0:
        print("X is 8")
    case 8:
        print("X is 8")
    case _:
        print("X is",x)
        
y=int(input("Enter Number:"))

match y:
    case 0:
        print("y is 0")
    case _ if(y!=80):
        print(y,"is not 80")
    case _ if(y!=90):
        print(y,"is not 90")
    case _:
        print(y)

z=4

match z:
    case 0:
        print("y is zero")
    case 4 if x % 2 == 0:
        print("x % 2 ==0 and case is 4")
    case _ if x < 10:
        print("x is < 10")
    case _:
        print(x)
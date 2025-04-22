#here lname is default argument and fname is required arguents
def name(fname,lname="Panchal"):
    print("Hello,",fname,lname)
    
name("Kapish")
#here fname is keyword argument
name(fname="Kip")

def fullname(fname,mname,lname):
    print("Hello,",fname,mname,lname)
#this is the example of keyword arguments
fullname(mname="Indravadanbhai",lname="Panchal",fname="Kapish")

#examples variable length arguments

def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)

c=average(5,5)
print(c)

def name(**name):
    print("Hello,",name['fname'],name['lname'])
    
name(lname="Panchal",fname="Kapish")
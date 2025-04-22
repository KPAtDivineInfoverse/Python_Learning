def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
    
def isGreater(a,b):
    if(a>b):
        print("First number is greater.")
    else:
        print("Second number is greater.")
        
a = 8
b = 10

calculateGmean(a,b)
isGreater(a,b)

c = 11
d = 5

calculateGmean(c,d)
isGreater(c,d)
print("Script is running...")

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        return "Error! Division by zero."
    return a/b

def calculator():
    print("Simple Calculator")
    print("Select An Operation")
    print("1. Add")
    print("2. Sub")
    print("3. Mul")
    print("4. Div")

    choice = input("Enter Your Choice (1/2/3/4)")

    if choice not in ('1','2','3','4'):
        print("Invalid Input")
        return 
    
    try:
        num1=float(input("Enter No 1."))
        num2=float(input("Enter No 2."))
    except ValueError:
        print("Invalid Number ")
        return 
    
    if choice == '1':
        print(f"The Result Is {add(num1,num2)}")
    elif choice == '2':
        print(f"The Result Is {sub(num1,num2)}")
    elif choice == '3':
        print(f"The Result Is {mul(num1,num2)}")
    elif choice == '4':
        print(f"The Result Is {div(num1,num2)}")

    if __name__ == "__main__":
        calculator()
        
calculator()  # <-- Directly calling the function here
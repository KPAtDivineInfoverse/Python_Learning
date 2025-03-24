# import google.generativeai as genai

# # Configure the API key
# genai.configure(api_key="AIzaSyDDDX39h_9tNE3o5Mv3Awj8ZluRrqckhJI")

# # Use the correct model
# model = genai.GenerativeModel("gemini-1.5-flash")

# # Generate content
# response = model.generate_content("how to make add to cart in laravel mysql")

# # Print response
# print(response.text)

a=int(input("Enter Age:"))
print("Your age is:",a)

if(a>18):
    print("You are 18+")
else:
    print("You are not 18+")
    
    
num=int(input("Enter num:"))

if(num<0):
    print("Num is Negative.")
elif(num == 0):
    print("Num is Zero.")
elif(num == 786):
    print("Num is special")
else:
    print("Num is Positive.")
    
print("Out of if-elif-else Statement.")


num1=18

if(num1<0):
    print("Num is negative")
elif(num1>0):
    if(num1<=10):
        print("Num is between 1-10.")
    elif(num1>10 and num1<=20):
        print("Num is between 11-20.")
    else:
        print("Num is greater than 20.")
else:
    print("Num is zero.")

# import time

# # timestamp = time.strftime("%H:%M:%S")
# # print(timestamp)  
# timestamp = int(time.strftime("%H"))
# print(timestamp)  
# # timestamp = int(time.strftime("%M"))
# # print(timestamp)  
# # timestamp = int(time.strftime("%S"))
# # print(timestamp)  

# if(timestamp>=6 and timestamp<12):
#     print("Good Morning")
# elif(timestamp>=12 and timestamp<6):
#     print("Good Afternoon")
# elif(timestamp>=6 and timestamp<9):
#     print("Good Evening")
# else:
#     print("Good Night")
    
import time

timestamp = int(time.strftime("%H"))
print(timestamp)

if 6 <= timestamp < 12:
    print("Good Morning")
elif 12 <= timestamp < 18:
    print("Good Afternoon")
elif 18 <= timestamp < 21:
    print("Good Evening")
else:
    print("Good Night")

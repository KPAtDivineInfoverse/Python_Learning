# for i in range(12):
#     if(i == 10):
#         break
#     print('5 x', i+1, "=", 5 * (i+1))
    
# print("Outside of the loop.")

for j in range(12):
    if(j == 10):
        print("Skip the iteration")
        continue
    print('5 x', j, "=", 5 *j)
    
    
# do while loop emulate
x=0
while True:
    print(x)
    x=x+1
    if(x%100 == 0):
        break
    
    
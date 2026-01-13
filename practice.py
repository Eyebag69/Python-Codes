#while loop = unlimited times
#for loop = limited times

#for i in range(10):
    #print(i+1)

'''for i in range(50,100+1,2):
    print(i)'''  

'''for i in "Aashish":
    print(i)'''

'''import time
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!!")'''  

#nested loop = inner loop will finish all of its iterations before finishing one iteration of the outer loop

'''rows = int(input("how many rows:"))
columns = int(input("How many columms:"))
symbol = input("Enter the symbol:")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()'''

'''for i in range(1,5):
    for j in range(i):
        print("*", end="")
    print()'''  

#loop control statement = change a loops execution from its normal sequence
# break = used to terminate a loop entirely 
# continue = skips the next iteration of loop
# pass = does nothing acts as a placeholder

'''while True:
    name = input("enter your name:")
    if name != "":
        break'''

phone_number = "123-456-7890"

'''for i in phone_number:
    if i == "-":
        continue
    print(i, end="")''' 

'''for i in range(1,21):
    if i == 13:
        pass 
    else:
        print(i)''' #skipped 13 and since if block gets executed and else part gets skipped, the value 13 gets skipped. 





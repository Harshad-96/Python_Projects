import random

number = random.randint(1,100)
while True:
 try:
   useNo = int(input("Enter the Number between 1 to 100: "))
   
   if useNo > 100:
    print("Number is not valid!")
   elif number > useNo :
    print("number is bigger than",useNo)
   elif number < useNo :
    print("the number is smaller than",useNo)
   else :
    print("Well done!")
    break
 except ValueError:
    print("Please enter valid number!")
    
     
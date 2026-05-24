print("CALCULATOR")
print("1- addition")
print("2- substraction")
print("3- division")
print("4- multiplication")
option = int(input("Choose operation of choice"))
if option in [1,2,3,4]:
   
       numb1 = int(input("ENTER THE FIRST NUMBER"))
       numb2 = int(input("ENTER THE SECOND NUMBER"))
       if option == 1:
          result = numb1 + numb2
       elif option == 2:
          result = numb1 - numb2
       elif option == 3:
          result = numb1/numb2 
       elif option == 4:
          result = numb1 * numb2
       print("THE RESULT : ",result)
else:
    print("INVALID")

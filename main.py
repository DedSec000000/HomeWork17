x = int(input("Give me a number that is even and also does not end with a 0: "))
if x >= 1000 and x <= 9999:
    if x%2 == 0:
       print("is good because it is even")
       if x%10 == 0:
          print("Is bad because it ends with 0")
       else:
            print("that is correct")
    else:
         print("is bad because it is bot given")
else:
    print("is bad because it is  not a 4 digit")
#LEVEL 1 WHILE LOOP
# while True:
#    secret_number = 55
#
#    guess = int(input('Enter the number : '))
#    if guess == secret_number:
#        print("congratulations your guess is correct")
#        break
#    else:
#      print("Your guess is wrong")

#LEVEL 1 FOR LOOP
# for i in range(0,7):
#      secret_number = 55
#
#      guess = int(input('Enter the number : '))
#      if guess == secret_number:
#         print("congratulations your guess is correct")
#         break
#      else:
#          print("Your guess is wrong")

#LEVEL 2
secret_number = 55
for i in range(0,8):
     user_input = int(input('Enter the number : '))
     if user_input < 1 or user_input > 100:
        print("Invalid number! Enter the number between 1 to 100")
     elif user_input > secret_number:
         print("Your number is high")
     elif user_input < secret_number:
         print("Your number is low")
     else:
         print("Your number is correct")
         break
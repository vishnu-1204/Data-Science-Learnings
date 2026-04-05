# for i in range(0,7):
#     secret_number = 55
#
#     guess = int(input('Enter the number : '))
#     if(guess == secret_number):
#         print("congratulations your guess is correct")
#         break
#     else:
#         print("Your guess is wrong")

while True:
    secret_number = 55

    guess = int(input('Enter the number : '))
    if guess == secret_number:
        print("congratulations your guess is correct")
        break
    else:
        print("Your guess is wrong")

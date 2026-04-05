secret_number = 55

guess = int(input('Enter the number : '))

if(guess == secret_number):
    print("congratulations your guess is correct")
else:
    print("Your guess is wrong")
import random

# Numbers to guess from
number = random.randint(1, 10)

# Introduce user
player_name = input('Hello player, please tell me your name.')
number_of_guesses = 0
print('Okay '+ player_name+ ' I am Guessing a number between 1 and 10:')

# While Loop
while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print( 'WRONG! Your guess is too low. Try again.')
    if guess > number:
        print ('WRONG! Your guess is too high. Try again.')
    if guess == number:
        break

# Verifying if the player guessed the number or not
if guess == number:
    print('CORRECT!!! You guessed the number in ' + str(number_of_guesses) + ' tries! Congrats!')
else:
    print('WRONG!!! You did not guess the number, The number was ' + str(number))
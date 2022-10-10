#number guess
import random

tries = 0
imaginedNumber = random.randint(1,20)

print('Hello! My name is Lavon. And what is your name?')
usersName = input()

print('Well, ' + usersName + ', I\'ve just imagined a number between 1 and 20. Would you like to try to guess it? You\'ve got three tries.')

for tries in range(3):
    print('Take a guess! Insert your number:')
    tryNumber = input()
    tryNumber = int(tryNumber)
    if tryNumber < imaginedNumber:
        print('Your guess is too low.')
    if tryNumber > imaginedNumber:
        print('Your guess is too high.')
    if tryNumber == imaginedNumber:
        break

if tryNumber == imaginedNumber:
    tries = str(tries + 1)
    print('Good job, ' + usersName + ', you guessed my number in ' + tries + ' guesses!')

if tryNumber != imaginedNumber:
    imaginedNumber = str(imaginedNumber)
    print('The number I was thinking of was ' + imaginedNumber + '. The game is over. Goodbye!')
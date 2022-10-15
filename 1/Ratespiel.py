#number guess
import random

imaginedNumber = random.randint(1,20) #legt eine beliebige Zufallszahl zwischen 1 und 20 fest

print('Hello! My name is Riddle. And what is your name?')
user_name = input()

print('Well, ' + user_name + ', I\'ve just imagined a number between 1 and 20. Would you like to try to guess it? You\'ve got three tries.')

for tries in range(3):
    print('Take a guess! Insert your number:')
    tryNumber = input()
    tryNumber = int(tryNumber)
    if tryNumber < imaginedNumber:
        print('Your guess is too low.')
    if tryNumber > imaginedNumber:
        print('Your guess is too high.')
    if tryNumber == imaginedNumber:
        print('This is right!!! YTou are the winner!')
        print('Gamer over!')
        exit()

print('Hey '+user_name+', unfortunately this time you lost! Sorry!')
print('Game over!')
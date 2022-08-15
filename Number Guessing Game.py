import random
import time

random_num = random.randint(1, 100)


def number_guess_game():
    tries = 0
    while tries <= 7:
        tries += 1
        current_guess = int(input("Guess a number between 1 and 100 "))
        if tries == 7:
            print("You're Tries are up. Thank you for playing!")
            time.sleep(1)
            break
        if current_guess > random_num:
            print("Your guess is higher")
            time.sleep(1)
        elif current_guess < random_num:
            print('Your Guess is lower')
            time.sleep(1)
        elif current_guess == random_num:
            print('Woohoo! You did it')
            time.sleep(1)
            break


print("Hey, Welcome to the Number Guessing Game!")
time.sleep(2)
print('The Rules are very simple, All you have to do is guess a number and the computer '
      'will tell you if you guessed higher or lower')
time.sleep(2)
print('You only have 7 tries')
time.sleep(2)
ready = input('Are you ready to play? (yes/no) ')

if ready == 'yes':
    number_guess_game()
else:
    print('Let me know when your ready :)')

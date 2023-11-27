# Created by Dorian at 25/11/2023
#import random
guessed, secret_number = False, None

def generate_number(dif):
    #random integer number between 0 and difficulty variable
    global secret_number
    secret_number = random.randint(0, int(dif))

def get_guess_from_user(dif):
    global user_guess
    user_guess = input(f'Please enter the integer number between 0 and {dif} in order to play the game: ')

def compare_results(secret_number, user_guess):
    global guessed
    #comparing the user input with the generated number
    if secret_number == int(user_guess):
        guessed = True
    else:
        guessed

def play(diff):
    generate_number(diff)
    get_guess_from_user(diff)
    compare_results(secret_number, user_guess)

    if guessed == True:
        print("CONGRATULATIONS!! You guessed the right number. YOU WON THE GAME!")
    else:
        print(f'That\'s a wrong guess :(. Generated number is: {secret_number}')
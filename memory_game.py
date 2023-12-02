# Created by Dorian at 26/11/2023
import random, functools,os, utils
from time import sleep

rand_list, guessed = [], False

def generate_sequence(dif):
    global rand_list
    #generating the random list with difficulty as a number of elemnts in the list
    for n in range(int(dif)):
        rand_list.append(random.randint(1,101))
    #printing the generated list for a certain amount of time
    if dif == '4':
        print("You have 0.5 seconds to remember the list\n")
        print(rand_list)
        sleep(0.5)
        utils.screen_cleaner()
    elif dif == '1':
        print("You have 2 seconds to remember the list\n")
        print(rand_list)
        sleep(2)
        utils.screen_cleaner()
    elif dif == '2':
        print("You have 1.5 seconds to remember the list\n")
        print(rand_list)
        sleep(1.5)
        utils.screen_cleaner()
    elif dif == '3':
        print("You have 1 second to remember the list\n")
        print(rand_list)
        sleep(1)
        utils.screen_cleaner()
    return rand_list

def get_list_from_user(dif):
    global user_guess
    print(f'Please enter the integer number between 1 and 101 in order to play the game. Number of elements is {dif}.\n')
    user_guess=[]
    user_guess = list(map(int, input("\nEnter the elemnts of a list : ").strip().split()))[:int(dif)]
    return user_guess

def is_list_equal(rand_list, user_guess):
    global guessed
    #using map and reduce to compare if the user input is the same
    if functools.reduce(lambda x,y : x and y, map(lambda p,q: p==q, rand_list,user_guess), True):
        guessed = True
        print(f'Comparison result:{guessed}')
        return guessed
    else:
        print(f'Comparison result:{guessed}')
        return guessed



def play(dif):
    generate_sequence(dif)
    get_list_from_user(dif)
    is_list_equal(rand_list,user_guess)

    if guessed == True:
        print("CONGRATULATIONS!! You guessed the right amount. YOU WON THE GAME!")
        return guessed
    else:
        print(f'That\'s a wrong guess :(. Correct answer is: {rand_list}')
        return guessed
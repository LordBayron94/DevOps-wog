# Created by Dorian at 02/09/2023
import guess_game, currency_roulette_game, memory_game, score, utils
import os.path as op, os, platform, random, urllib.request, functools, datetime
from currency_converter import ECB_URL, CurrencyConverter
from time import sleep
from datetime import date

def welcome():
    username = input("Please enter your name here:")
    print(f'Hello {username} and welcome to the World of Games: The Epic Journey\n')

def start_play():
    #define the dictionary of playable games
    Games={
        '1': 'Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back',
        '2': 'Guess Game - guess a number and see if you chose like the computer.',
        '3': 'Currency Roulette - try and guess the value of a random amount of USD in ILS'
    }
    
    #printing the playeble options
    for key, value in Games.items():
        print(key, ':', value)
    
    #selecting the game from the given list
    selected_game = input('\nPlease select one of the games from the list by entering the number:')
    
    #printing the name of the selected game and what is this game about
    for key, value in Games.items():
        #case where we have the right number from the given list
        if selected_game == key:
            print(f'Selected game is: {value}.\n We\'re starting the game....\n')
            #starting the game
            if selected_game == '1':
                diff = input(f'Enter a non zero difficulty level: ')
                currency_roulette_game.play(diff)
                break
            elif selected_game == '2':
                diff = input(f'Enter a non zero difficulty: ')
                guess_game.play(diff)
                break
            elif selected_game == '3':
                diff = input(f'Max difficulty is 4! Please enter a non zero difficulty: ')
                memory_game.play(diff)
                break
            else:
                break
            print("Game over!")
            break
        #case where we don't have the right number and the number our user has entered is within the length of the defined dictionary
        #we want to continue until user has picked the right number
        elif selected_game != key and int(key) < len(Games):
            continue
        #case where user entered wrong number outside the given options
        #implemented the recursion so that user can see the list and enter the corret option
        elif int(selected_game) == 0 or selected_game != key:
            print('\nEntered number is not defined in the list, please try again!\n')
            start_play()


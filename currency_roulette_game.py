# Created by Dorian at 25/11/2023
from currency_converter import ECB_URL, CurrencyConverter
from datetime import date
import random, urllib.request
import os.path as op

c, secret_number, guessed, correct_answ_interval = 0,0,False,None

def get_money_interval(diff):
    global secret_number, c
    #generating radnom value for the emount of $
    secret_number = random.randint(0, 100)

    #applying API Currency Converter and downloading raw data for a up-to-date info!
    filename = f"ecb_{date.today():%Y%m%d}.zip"
    if not op.isfile(filename):
        urllib.request.urlretrieve(ECB_URL, filename)
    curr = CurrencyConverter(filename)
    c = curr.convert(secret_number, 'USD', 'ILS')

    #calculating correct answer interval
    global correct_answ_interval
    correct_answ_interval = 10 - int(diff)
    print(f'Your inputed guess will be correct if it\'s by {correct_answ_interval} higher or lower than the true value!')

def get_guess_from_user(secret_number):
    global user_guess
    user_guess = input(f'Please enter how much would {secret_number}$ be in ILS')
    return user_guess

def compare_results(c,user_guess, correct_answ_interval):
    global guessed
    # comparing the user input with the generated number
    if c == int(user_guess) or c+correct_answ_interval <= int(user_guess) or c-correct_answ_interval >= int(user_guess):
        guessed = True
    else:
        return guessed

def play(diff):
    get_money_interval(diff)
    get_guess_from_user(secret_number)
    compare_results(c, user_guess, correct_answ_interval)

    if guessed == True:
        print("CONGRATULATIONS!! You guessed the right amount. YOU WON THE GAME!")
    else:
        print(f'That\'s a wrong guess :(. Correct conversion is: {c}')
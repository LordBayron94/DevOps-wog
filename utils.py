# Created by Dorian at 27/11/2023
import platform, os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 404

def screen_cleaner():
    print(platform.platform(aliased=True))
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
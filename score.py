# Created by Dorian at 27/11/2023
import os.path as op, utils, datetime

POINTS_OF_WINNING = None

def add_score(dif):
    global POINTS_OF_WINNING
    POINTS_OF_WINNING = (int(dif)*3)+5
    #checking if the Scores.txt exists
    if not op.isfile(f'{utils.SCORES_FILE_NAME}'):
        print('File doesn\'t exist! Creating the new file\n')
        #creating the file
        with open(f'{utils.SCORES_FILE_NAME}', mode='a') as f:
            f.write(f'Score %s recorded at %s: {POINTS_OF_WINNING}')
        f.close()
    else:
        #writing the score in the existing file
        print(f'Writing score in {utils.SCORES_FILE_NAME}')
        with open(f'{utils.SCORES_FILE_NAME}', mode='a') as f:
            f.write(f'Score recorded: {POINTS_OF_WINNING}\n')
            f.close()


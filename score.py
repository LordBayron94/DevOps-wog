# Created by Dorian at 27/11/2023
import os.path as op, utils, datetime

POINTS_OF_WINNING, SCORES_FILE_NAME = None, "Scores.txt"

def add_score(dif):
    global POINTS_OF_WINNING
    POINTS_OF_WINNING = (dif*3)+5
    #checking if the Scores.txt exists
    if not op.isfile(f'data/{utils.SCORES_FILE_NAME}'):
        print('File doesn\'t exist! Creating the new file\n')
        #creating the file
        with open(f'data/{utils.SCORES_FILE_NAME}', mode='a') as f:
            f.write('Score %s recorded at %s:\t' % (POINTS_OF_WINNING, datetime.datetime.now()))
        f.close()
    else:
        #writing the score in the existing file
        print(f'Writing score in {utils.SCORES_FILE_NAME}')
        with open(f'data/{utils.SCORES_FILE_NAME}', mode='a') as f:
            f.write('Score %s recorded at %s:\t' % (POINTS_OF_WINNING, datetime.datetime.now()))
            f.close()


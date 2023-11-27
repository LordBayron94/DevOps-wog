# Created by Dorian at 27/11/2023
import os.path as op, utils, datetime

POINTS_OF_WINNING = None

def add_score(dif):
    global POINTS_OF_WINNING
    POINTS_OF_WINNING = (dif*3)+5
    #checking if the Scores.txt exists
    if op.isfile(f'G:/Global Dev Experts/Projects/wog/data/{utils.SCORES_FILE_NAME}') == False:
        print('File doesn\'t exist! Creating the new file\n')
        #creating the file
        f = open(f'G:/Global Dev Experts/Projects/wog/data/{utils.SCORES_FILE_NAME}', "x")
        f.write(POINTS_OF_WINNING)
        f.close()
    else:
        print(f'Writing score in {utils.SCORES_FILE_NAME}')
        with open(f'G:/Global Dev Experts/Projects/wog/data/{utils.SCORES_FILE_NAME}', mode='a') as f:
            f.write('Score %s recorded at %s:\t' % (POINTS_OF_WINNING, datetime.datetime.now()))


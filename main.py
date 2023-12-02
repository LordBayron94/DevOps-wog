from app import welcome, start_play
from flask import Flask
import os.path as op, datetime

app = Flask(__name__)

def get_file():
    if not op.isfile(f'Scores.txt'):
        print('File doesn\'t exist! Creating the new file\n')
        return f'Error'
    else:
        with open('Scores.txt', 'r') as f:
            score = f.read().strip
        return score

@app.route('/WoG')
def score_server():
    user_score = get_file()

    if user_score.startswith("Error"):
        content = f'''
        <html>
            <head>
                <title>Scores Game</title>
            </head>
        <body>
            <h1>ERROR</h1>
            <div id="score" style="color:red">{user_score}</div>
        </body>
        </html>
        '''
    else:
        content=f'''
        <html>
            <head>
                <title>Scores Game</title>
            </head>
        <body>
            <h1>The score is:</h1>
            <div id="score">{user_score}</div>
        </body>
        </html>
        '''
    return content

if __name__ == '__main__':
    welcome()
    start_play()
    app.run(debug=False)

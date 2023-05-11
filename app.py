from flask import Flask, request
import random
app = Flask(__name__)


@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    client_move = data['move']
    server_move = random.choice(['rock', 'paper', 'scissors'])
    if client_move == server_move:
        result = 'tie'
    elif client_move == 'rock' and server_move == 'scissors' or \
            client_move == 'paper' and server_move == 'rock' or \
            client_move == 'scissors' and server_move == 'paper':
        result = 'win'
    else:
        result = 'lose'
    return {'result': result, 'server_move': server_move}


if __name__ == "__main__":
    app.run(port=5000, debug=True)

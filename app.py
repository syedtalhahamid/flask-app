from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'  # Needed for session security
socketio = SocketIO(app)

@app.route('/')
def chat():
    return render_template('chat.html')

@socketio.on('message')
def handleMessage(msg):
    print('Message:', msg)
    send(msg, broadcast=True)  # Sends to all connected clients

if __name__ == '__main__':
    socketio.run(app, debug=True)

import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('connection established')


@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})


@sio.event
def disconnect():
    print('disconnected from server')


@sio.event
def login(data):
    print(data)


sio.connect('http://localhost:3000')
sio.emit('login', {'username': 'Omar', 'password': '01060120066'})
sio.wait()

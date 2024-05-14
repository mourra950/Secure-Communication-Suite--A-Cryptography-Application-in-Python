import socketio
import SHAversion2

class Sockets(socketio.simple_client):
    

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
def loginResponse(data):
    print(data)


sio.connect('http://localhost:3000')
t=SHAversion2.hash_sha256("123")

sio.emit('login', {'username': 'test', 'password': t})
sio.wait()

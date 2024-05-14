import socketio
import SHAversion2


class SocketsIO(socketio.simple_client):
    def __init__(self):
        self.sio = socketio.Client()
        self.sio.connect('http://localhost:3000')

    def callbacks(self):
        @self.sio.event
        def connect():
            print('connection established')

        @self.sio.event
        def loginResponse(data):
            print(data)

        @self.sio.event
        def disconnect():
            print('disconnected from server')

        @self.sio.event
        def my_message(data):
            print('message received with ', data)

    def socket_login(self, username, password):
        hashedPassword = SHAversion2.hash_sha256(password)
        self.sio.emit('login', {'username': username,
                      'hashedPassword': hashedPassword})

    def socket_signup(self, username, password, publicKey):
        hashedPassword = SHAversion2.hash_sha256(password)
        self.sio.emit('login', {'username': username,
                      'hashedPassword': hashedPassword, "publicKey": publicKey})

import socketio
import SHAversion2
from PySide6.QtWidgets import (
    QVBoxLayout,
    QMainWindow,
    QApplication,
    QPushButton,
    QLineEdit,
    QDialog,
    QLabel,
    QFileDialog
)
from PySide6.QtWidgets import QFileDialog
from PySide6.QtUiTools import QUiLoader
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
from PySide6.QtCore import Signal, QObject


class PrintDialog(QDialog):

    def __init__(self, text):
        # super(PrintDialog, self).__init__()
        self.setWindowTitle("Output")
        self.layout = QVBoxLayout()
        self.label = QLabel(text)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.label)
        self.ok_button = QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        self.layout.addWidget(self.ok_button)
        self.setLayout(self.layout)
        self.exec()


class SocketsIO(QObject):

    switch = Signal()
    read_message = Signal(dict)
    users = Signal(list)

    def __init__(self):
        QObject.__init__(self)
        # print(self)
        self.sio = socketio.Client()
        self.sio.connect('https://secure-communication-suite-server.onrender.com/')
        self.callbacks()

    def run(self):
        try:
            self.sio.connect('https://secure-communication-suite-server.onrender.com/')
            self.callbacks()
        except:
            self.switch.emit()

    def callbacks2(self, text):
        @self.sio.on(f"readMessage_{text}")
        def readMessage(response):
            print(response)
            self.read_message.emit(response)

    def callbacks(self):
        @self.sio.event
        def connect():
            print('connection established')

        @self.sio.event
        def loginResponse(data):
            print(data)
            if data['success'] == True:
                print(data['user']['username'])
                self.callbacks2(data['user']['username'])
                self.switch.emit()

        @self.sio.event
        def signupResponse(data):
            print(data)

        @self.sio.event
        def disconnect():
            print('disconnected from server')

        @self.sio.event
        def my_message(data):
            print('message received with ', data)

        @self.sio.event
        def getAllUsersResponse(data):
            # print(data)

            self.users.emit(data["users"])

        @self.sio.event
        def readMessage(data):
            print(data)
            self.read_message.emit(data)

    def socket_login(self, username, password):
        hashedPassword = SHAversion2.hash_sha256(password)
        self.sio.emit('login', {'username': username,
                      'hashedPassword': hashedPassword})

    def socket_signup(self, username, password, publicKey):
        hashedPassword = SHAversion2.hash_sha256(password)
        self.sio.emit('signup', {'username': username,
                      'hashedPassword': hashedPassword, "publicKey": publicKey.decode('utf-8')})

    def request_all_users(self):
        self.sio.emit('getAllUsers')

    def send_message(self, cyphertext, cypherkey, user):
        # print(cyphertext,cypherkey)
        # print(cyphertext.decode('utf-8'),cypherkey.encode('utf-8'))
        # return
        self.sio.emit('message', {"cyphertext": cyphertext,
                      "cypherkey": cypherkey, "user": user})
        # send who am i ?

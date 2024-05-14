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


class PrintDialog(QDialog):
    def __init__(self, text):
        super(PrintDialog, self).__init__()
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


class SocketsIO():
    def __init__(self):
        self.sio = socketio.Client()
        self.sio.connect('http://localhost:3000')
        self.callbacks()

    def callbacks(self):
        @self.sio.event
        def connect():
            print('connection established')

        @self.sio.event
        def loginResponse(data):
            print(data)
            PrintDialog(data['message'])
            if data['success'] == True:
                self.switchpage()

        @self.sio.event
        def signupResponse(data):
            print(data)
            PrintDialog(data['message'])

        @self.sio.event
        def disconnect():
            print('disconnected from server')

        @self.sio.event
        def my_message(data):
            print('message received with ', data)

        @self.sio.event
        def getAllUsersResponse(data):
            print(data)
            self.all_users = data["users"]
            self.populate_user_list()

    def socket_login(self, username, password):
        hashedPassword = SHAversion2.hash_sha256(password)
        self.sio.emit('login', {'username': username,
                      'hashedPassword': hashedPassword})

    def socket_signup(self, username, password, publicKey):
        hashedPassword = SHAversion2.hash_sha256(password)
        self.sio.emit('signup', {'username': username,
                      'hashedPassword': hashedPassword, "publicKey": str(publicKey)})

    def request_all_users(self):
        self.sio.emit('getAllUsers')

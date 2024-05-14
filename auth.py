import os
import sys

from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
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
from PySide6 import QtCore
from DB import DB
import RSA
import hashlib


basedir = os.path.dirname(__file__)
loader = QUiLoader()


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


class AuthUI(DB):
    def __init__(self):
        self.auth_window = loader.load(os.path.join(basedir, "auth.ui"), None)
        self.auth_window.setWindowTitle("Authentication")
        self.auth_find_children()
        self.auth_setup_btn()

    def auth_find_children(self):
        self.qt_username_line = self.auth_window.findChild(
            QLineEdit, "username_lineEdit")
        self.qt_password_line = self.auth_window.findChild(
            QLineEdit, "password_lineEdit")
        self.qt_new_btn = self.auth_window.findChild(
            QPushButton, "newUser_btn")
        self.qt_auth_btn = self.auth_window.findChild(
            QPushButton, "authenticateUser_btn")
        self.qt_switch_btn = self.auth_window.findChild(
            QPushButton, "SwitchButton")

    def auth_setup_btn(self):
        self.qt_new_btn.clicked.connect(self.new_user)
        self.qt_auth_btn.clicked.connect(self.authenticate_user)
        self.qt_switch_btn.clicked.connect(self.switchpage)

    def switchpage(self):
        self.auth_window.close()
        self.window_chat.show()

    def hash_sha256(self, plaintext):
        hasher = hashlib.new("SHA256")
        hasher.update(plaintext.encode())
        return str(hasher.hexdigest())

    def new_user(self):
        username = self.qt_username_line.text()
        password = self.qt_password_line.text()
        temp = RSA.RSA_Task()
        public = temp.rsa_public_key
        private = temp.rsa_private_key

        self.socket_signup(username, password, public.n)

        # path, _ = QFileDialog.getSaveFileName(
        #     self.window, "Save Public Key", "./key/", "PEM (*.pem)")
        # with open(path, "wb+") as f:
        #     f.write(str(private.d).encode())
        # hash_password = self.hash_sha256(password)
        # user = {
        #     'username': username,
        #     'password': hash_password,
        # }

        # self.users.insert_one(user)
        # self.keys.insert_one({'username': username, 'key': str(public.n)})
        # PrintDialog(f"user {user}, added")

    def authenticate_user(self):
        username = self.qt_username_line.text()
        password = self.qt_password_line.text()
        self.socket_login(username, password)


def main():
    app = QApplication(sys.argv)
    window = AuthUI()
    app.exec()


if __name__ == "__main__":
    main()

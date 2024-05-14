import os
import sys

from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QLineEdit,
    QFileDialog
)
from PySide6.QtWidgets import QFileDialog
from PySide6.QtUiTools import QUiLoader

import RSA
import hashlib


basedir = os.path.dirname(__file__)
loader = QUiLoader()


class AuthUI():
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
        self.SocketsIO.request_all_users()

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

        self.SocketsIO.socket_signup(username, password, public.n)

        path, _ = QFileDialog.getSaveFileName(
            self.window, "Save Public Key", "./key/", "PEM (*.pem)")
        with open(path, "wb+") as f:
            f.write(str(private.d).encode())

    def authenticate_user(self):
        username = self.qt_username_line.text()
        password = self.qt_password_line.text()
        self.SocketsIO.socket_login(username, password)


def main():
    app = QApplication(sys.argv)
    window = AuthUI()
    app.exec()


if __name__ == "__main__":
    main()

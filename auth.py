import os
import sys

from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QVBoxLayout,
    QMainWindow,
    QApplication,
    QPushButton,
    QComboBox,
    QTextEdit,
    QLineEdit,
    QDialog,
    QLabel

)
from PySide6.QtWidgets import  QFileDialog
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
from PySide6.QtCore import QThreadPool
from DB import DB

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

class AuthUI(QMainWindow,DB):
    def __init__(self):
        QMainWindow.__init__(self)
        # DB.__init__(self)
        self.window = loader.load(os.path.join(basedir, "auth.ui"), None)
        self.window.setWindowTitle("Authentication")        
        self.find_children()
        self.setup_btn()
        self.window.show()


    def find_children(self):
        self.qt_username_line = self.window.findChild(QLineEdit, "username_lineEdit")
        self.qt_password_line = self.window.findChild(QLineEdit, "password_lineEdit")

        self.qt_new_btn = self.window.findChild(QPushButton, "newUser_btn")
        self.qt_auth_btn = self.window.findChild(QPushButton, "authenticateUser_btn")
        
    def setup_btn(self):
        self.qt_new_btn.clicked.connect(self.new_user)
        self.qt_auth_btn.clicked.connect(self.authenticate_user)
        
    def hash_sha256(self,plaintext):
        hasher = hashlib.new("SHA256")
        hasher.update(plaintext.encode())
        return str(hasher.hexdigest())
        
    def new_user(self):
        username = self.qt_username_line.text()
        password = self.qt_password_line.text()

        if self.users.find_one({'username':username}) != None:
            PrintDialog("user found")
            return
        hash_password = self.hash_sha256(password)
        user = {
            'username':username,
            'password':hash_password
        }    
        self.users.insert_one(user)
        PrintDialog(f"user {user}, added")
    
    def authenticate_user(self):
        username = self.qt_username_line.text()
        password = self.qt_password_line.text()
        hash_password = self.hash_sha256(password)

        if self.users.find_one({'username':username,'password':hash_password}) != None:
            PrintDialog("user authenticated")
        else:
            PrintDialog("user not found")
            
def main():
    app = QApplication(sys.argv)
    window = AuthUI()
    app.exec()


if __name__ == "__main__":
    main()

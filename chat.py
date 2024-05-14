import os
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QTextEdit,
    QSizePolicy
)

from PySide6.QtUiTools import QUiLoader

from sockets import SocketsIO
from auth import AuthUI

basedir = os.path.dirname(__file__)
loader = QUiLoader()


class MainUI(QMainWindow, AuthUI):

    def __init__(self):
        QMainWindow.__init__(self)

        AuthUI.__init__(self)
        self.window_chat = loader.load(
            os.path.join(basedir, "window_chat.ui"), None)
        self.Conditions = True
        self.current_user = ""
        self.window_chat.setWindowTitle("Chat")
        self.chat_findchildreen()
        self.chat_setup()
        self.all_users = []

        self.populate_user_list(self.all_users)
        self.auth_window.show()

        self.SocketsIO = SocketsIO()
        self.SocketsIO.switch.connect(self.switchpage)
        self.SocketsIO.users.connect(self.populate_user_list)

    def chat_findchildreen(self):
        self.qt_left_scroll = self.window_chat.findChild(
            QVBoxLayout, "Button_vertical")
        self.qt_Message_scroll = self.window_chat.findChild(
            QVBoxLayout, "Messages_layouts")
        self.qt_user_label = self.window_chat.findChild(QLabel, "User_label")
        self.qt_send_btn = self.window_chat.findChild(QPushButton, "Send_btn")
        self.qt_message_area = self.window_chat.findChild(
            QTextEdit, "Message_Area")

    def chat_setup(self):
        self.qt_send_btn.clicked.connect(self.sendMessage)

    def sendMessage(self):
        message = self.qt_message_area.toPlainText()
        print(f"Message from {self.current_user}: {message}")
        self.qt_message_area.clear()
        temp = QLabel(f"{self.current_user}: {message}")
        # temp.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        if self.Conditions == True:
            temp.setStyleSheet("background-color: rgb(0, 255, 0);")
            temp.setAlignment(Qt.AlignLeft)

            self.Conditions = False
        else:
            temp.setStyleSheet("background-color: rgb(255, 0, 0);")
            temp.setAlignment(Qt.AlignRight)
            self.Conditions = True
        self.qt_Message_scroll.addWidget(temp)

    def populate_user_list(self, users):
        self.all_users = users
        for i in self.all_users:
            temp = QPushButton(f"{i['username']}")
            temp.clicked.connect(lambda func=self.setMessage, pub=i["key"],
                                 user=i['username']: func(user, pub))
            self.qt_left_scroll.addWidget(temp)

    def setMessage(self, User, Public):
        # print(User)
        self.qt_user_label.setText(f"{User}, {Public}")
        self.pub_key = Public
        self.current_user = User


# done


def main():
    app = QApplication(sys.argv)
    window = MainUI()
    app.exec()


if __name__ == "__main__":
    main()

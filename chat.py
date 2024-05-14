import os
import sys
# from PySide6 import QtWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt
import socketio
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QScrollArea, QVBoxLayout, QPushButton, QLabel, QTextEdit, QSizePolicy
)


from PySide6.QtUiTools import QUiLoader


user_list = ["ahmed", "Mohamed", "Yousef"]


basedir = os.path.dirname(__file__)
loader = QUiLoader()


class MainUI(QMainWindow):
    
    def __init__(self):
        self.sio=socketio.Client()
        
        QMainWindow.__init__(self)
        self.Conditions = True
        self.current_user = ""
        self.window = loader.load(os.path.join(
            basedir, "window_chat.ui"), None)
        self.window.setWindowTitle("Chat")
        self.findchildreen()
        self.setup()

        self.fill_left()
        self.window.show()
        self.sio.connect('http://localhost:3000')
    def callback(self):
        @self.sio.event
        def connect():
            print('connection established')

    def findchildreen(self):
        self.qt_left_scroll = self.window.findChild(
            QVBoxLayout, "Button_vertical")
        self.qt_Message_scroll = self.window.findChild(
            QVBoxLayout, "Messages_layouts")
        self.qt_user_label = self.window.findChild(QLabel, "User_label")
        self.qt_send_btn = self.window.findChild(QPushButton, "Send_btn")
        self.qt_message_area = self.window.findChild(QTextEdit, "Message_Area")

    def setup(self):
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

    def fill_left(self):
        self.t = QVBoxLayout()
        for i in user_list:
            temp = QPushButton(f"{i}")
            temp.clicked.connect(lambda func=self.setMessage,
                                 user=i: func(user))
            self.qt_left_scroll.addWidget(temp)

    def setMessage(self, User):
        # print(User)
        self.qt_user_label.setText(User)
        self.current_user = User


# done


def main():
    app = QApplication(sys.argv)
    window = MainUI()
    app.exec()


if __name__ == "__main__":
    main()

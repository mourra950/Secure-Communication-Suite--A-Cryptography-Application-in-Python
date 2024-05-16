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
    QSizePolicy, QFileDialog
)

from PySide6.QtUiTools import QUiLoader

from sockets import SocketsIO
from auth import AuthUI
from RSA import RSA_Task
from AES import AES_Task
basedir = os.path.dirname(__file__)
loader = QUiLoader()


class MainUI(QMainWindow, AuthUI):

    def __init__(self):
        QMainWindow.__init__(self)
        self.RSA = RSA_Task()
        self.AES = AES_Task()
        self.message_dict = dict()
        self.users_data = None

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
        self.SocketsIO.read_message.connect(self.read_message)

    def read_message(self, data):
        ciphertext = data['cyphertext']
        cypherkey = data['cypherkey']
        user = data['sender']
        key_AES = self.RSA.RSA_Decrypt(
            private=self.private_key_bin, text=cypherkey)
        message = self.AES.AES_Decrypt(ciphertext=ciphertext, key_AES=key_AES)
        if user in self.message_dict:
            self.message_dict[user].append((message, 1))
        else:
            self.message_dict[user] = []
            self.message_dict[user].append((message, 1))
        self.show_messages()

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
        # self.message_dict[self.current_user].message_list = message
        if self.current_user in self.message_dict:
            self.message_dict[self.current_user].append((message, 0))
        else:
            self.message_dict[self.current_user] = []
            self.message_dict[self.current_user].append((message, 0))

        ciphertext, key = self.AES.AES_Encrypt(text=message)
        AES_Key_Cyphered = self.RSA.RSA_Encrypt(
            private=self.private_key_bin, public=self.pub_key, text=key)

        self.SocketsIO.send_message(
            cypherkey=AES_Key_Cyphered, cyphertext=ciphertext, user=self.current_user)

        self.qt_message_area.clear()
        self.show_messages()
        

    def read_private(self):
        binary = None
        path, _ = QFileDialog.getOpenFileName(
            None, "Open PEM File", "./key/", "PEM(*.pem)")
        with open(path, 'rb') as f:
            binary = f.read()
        self.private_key_bin = self.RSA.rsa_private_key.load_pkcs1(binary)
        print(self.private_key_bin)

    def populate_user_list(self, users):
        self.all_users = users
        for i in self.all_users:
            temp = QPushButton(f"{i['username']}")
            temp.clicked.connect(lambda func=self.set_second_client, pub=i["key"],
                                 user=i['username']: func(user, pub))
            self.qt_left_scroll.addWidget(temp)

    def set_second_client(self, User, Public):
        # print(User)
        self.qt_user_label.setText(f"{User}")
        # print()
        self.pub_key = self.RSA.rsa_public_key.load_pkcs1(Public)
        print(self.pub_key)
        self.current_user = User
        self.show_messages()

    def show_messages(self):
        while self.qt_Message_scroll.count() > 0:
            layout_item = self.qt_Message_scroll.takeAt(0)
            widget_to_remove = layout_item.widget()
            if widget_to_remove:
                widget_to_remove.deleteLater()
        if self.current_user in self.message_dict:

            for i in self.message_dict[self.current_user]:
                message, who = i

                if who == 0:
                    temp = QLabel(f"you: {message}")
                    temp.setStyleSheet("background-color: rgb(150, 255, 150);")
                    temp.setAlignment(Qt.AlignRight)
                else:
                    temp = QLabel(f"them: {message}")
                    temp.setStyleSheet("background-color: rgb(150, 150, 255);")
                    temp.setAlignment(Qt.AlignLeft)

                self.qt_Message_scroll.addWidget(temp)
        else:
            print('No messages')
# done


def main():
    app = QApplication(sys.argv)
    window = MainUI()
    app.exec()


if __name__ == "__main__":
    main()

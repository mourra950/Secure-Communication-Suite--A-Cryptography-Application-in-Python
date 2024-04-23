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
    QLineEdit

)
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
from PySide6.QtCore import QThreadPool

from Crypto.Cipher import AES
from encryptor import EncryptionWorker
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

import queue
import math
from AES import AES_Task
from encryptor3 import EncryptionWorker3
from encryptor4 import EncryptionWorker4

basedir = os.path.dirname(__file__)
loader = QUiLoader()


class MainUI(QMainWindow,AES_Task):
    def __init__(self):
        QMainWindow.__init__(self)
        AES_Task.__init__(self)
        self.window = loader.load(os.path.join(basedir, "security.ui"), None)
        self.window.setWindowTitle("Security")        
        # self.test = "Testing"
        # self.threadpool = QThreadPool()
        self.keysize = 16
        # self.initqueues()
        self.findchildreen()
        self.setup_combox()
        self.setup_btn()
        # self.initworker()
        self.window.show()
    def Threads(self):
        self.AES_Thread=AES_Task()
        
    def initqueues(self):
        self.plaintext_queue = queue.Queue()
        self.ciphertext_queue = queue.Queue()

    def initworker(self):
        self.worker = EncryptionWorker4(
            self.plaintext_queue, self.ciphertext_queue, self)
        self.threadpool.start(self.worker)
    def connections(self):
        self.qt_AES_btn.clicked.connect()
#done
    def findchildreen(self):
        self.qt_keysizeComboBox = self.window.findChild(QComboBox, "KeySizeComboBox")
        self.qt_cipher = self.window.findChild(QTextEdit, "CipherArea")
        self.qt_text = self.window.findChild(QTextEdit, "TextArea")        
        self.qt_key_line = self.window.findChild(QLineEdit, "Key_lineEdit")
        self.qt_AES_btn = self.window.findChild(QPushButton, "AES_btn")
        self.qt_AES_Dbtn = self.window.findChild(QPushButton, "AES_Dbtn")
        
        self.qt_DES_btn = self.window.findChild(QPushButton, "DES_btn")
        self.qt_ECC_btn = self.window.findChild(QPushButton, "ECC_btn")
        self.qt_MD5_btn = self.window.findChild(QPushButton, "MD5_btn")
        self.qt_SHA256_btn = self.window.findChild(QPushButton, "SHA256_btn")
        self.qt_RSA_btn = self.window.findChild(QPushButton, "RSA_btn")
#done
    def setup_combox(self):
        self.qt_keysizeComboBox.addItem("16", 16)
        self.qt_keysizeComboBox.addItem("24", 24)
        self.qt_keysizeComboBox.addItem("32", 32)
        self.qt_keysizeComboBox.currentIndexChanged.connect(self.key_onchange)
        
    def key_onchange(self):
        self.keysize = self.qt_keysizeComboBox.currentData()
    
    def setup_btn(self):
        self.qt_AES_btn.clicked.connect(self.AES_Encrypt)
        self.qt_AES_Dbtn.clicked.connect(self.AES_Decrypt)
        self.qt_DES_btn.clicked.connect(self.)
        
        # self.qt_ECC_btn.clicked.connect(self.)
        # self.qt_MD5_btn.clicked.connect(self.)
        # self.qt_SHA256_btn.clicked.connect(self.)
        # self.qt_encryptbutn.clicked.connect(self.encrypt_SHA)

    # def encrypt_AES(self):
    #     plaintext = self.qt_textarea.toPlainText()
    #     self.keysize = self.qt_keysizeComboBox.currentData()
    #     # print(plaintext, self.keysize, type(self.keysize))

    #     for i in range(math.ceil(len(plaintext)/self.keysize)):
    #         sclicedmessage = plaintext[0+self.keysize *
    #                                    i:self.keysize*i+self.keysize]
    #         self.plaintext_queue.put(sclicedmessage)
    #         # print(i,sclicedmessage)
    #     # print("Queued")

    # def encrypt_RSA(self):
    #     plaintext = self.qt_textarea.toPlainText()
    #     self.plaintext_queue.put(plaintext)

    # def encrypt_SHA(self):
    #     plaintext = self.qt_textarea.toPlainText()
    #     self.plaintext_queue.put(plaintext)


def main():
    app = QApplication(sys.argv)
    window = MainUI()
    app.exec()


if __name__ == "__main__":
    main()

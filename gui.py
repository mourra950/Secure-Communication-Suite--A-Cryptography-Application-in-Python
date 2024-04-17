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
    
)
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
from PySide6.QtCore import QObject, QRunnable, QThreadPool, QTimer, Signal, Slot

from Crypto.Cipher import AES
from encryptor import EncryptionWorker
from Crypto.Random import get_random_bytes
import queue
import math
from encryptor2 import EncryptionWorker2
basedir = os.path.dirname(__file__)
loader = QUiLoader()


class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.test="Testing"        
        self.threadpool = QThreadPool()
        self.initqueues()
        self.window = loader.load(os.path.join(basedir, "security.ui"), None)
        self.findchildreen()
        self.setup_combox()
        self.setup_encryptbtn()
        self.window.setWindowTitle("Security")
        self.initworker()

        self.window.show()
    def initqueues(self):
        self.plaintext_queue = queue.Queue()
        self.ciphertext_queue = queue.Queue()
        
    def initworker(self):
        self.worker = EncryptionWorker2(self.plaintext_queue,self.ciphertext_queue)
        self.threadpool.start(self.worker)
        
    def findchildreen(self):
        self.qt_keysizeComboBox = self.window.findChild(
            QComboBox, "KeySizeComboBox")
        self.qt_textarea = self.window.findChild(QTextEdit, "TextArea")
        self.qt_encryptbutn = self.window.findChild(QPushButton, "EncryptButn")

    def setup_combox(self):
        self.qt_keysizeComboBox.addItem("16", 16)
        self.qt_keysizeComboBox.addItem("24", 24)
        self.qt_keysizeComboBox.addItem("32", 32)

    def setup_encryptbtn(self):
        self.qt_encryptbutn.clicked.connect(self.encrypt)
        
        
    def encrypt(self):
        plaintext = self.qt_textarea.toPlainText()
        self.keysize = self.qt_keysizeComboBox.currentData()
        print(plaintext, self.keysize, type(self.keysize))
        
        for i in range(math.ceil(len(plaintext)/self.keysize)):
            sclicedmessage=plaintext[0+self.keysize*i:self.keysize*i+self.keysize]
            self.plaintext_queue.put(sclicedmessage)
            print(i,sclicedmessage)
        print("Queued")


def main():
    app = QApplication(sys.argv)
    window = MainUI()
    app.exec()


if __name__ == "__main__":
    main()

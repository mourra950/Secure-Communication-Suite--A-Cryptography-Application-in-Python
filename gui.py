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
from PySide6.QtWidgets import  QFileDialog

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
from DES import DES_Task

from RSA import RSA_Task

from SHA import SHA256_Task
from MD5 import MD5_Task

from ECC import ECC_Task



basedir = os.path.dirname(__file__)
loader = QUiLoader()


class MainUI(QMainWindow,AES_Task,RSA_Task,SHA256_Task,MD5_Task,DES_Task,ECC_Task):
    def __init__(self):
        QMainWindow.__init__(self)
        AES_Task.__init__(self)
        DES_Task.__init__(self)
        
        RSA_Task.__init__(self)
        ECC_Task.__init__(self)

        SHA256_Task.__init__(self)
        MD5_Task.__init__(self)
        self.window = loader.load(os.path.join(basedir, "security.ui"), None)
        self.window.setWindowTitle("Security")        
        self.keysize = 16
        self.findchildreen()
        self.setup_combox()
        self.setup_btn()
        self.window.show()
    def Threads(self):
        self.AES_Thread=AES_Task()
        
    def initqueues(self):
        self.plaintext_queue = queue.Queue()
        self.ciphertext_queue = queue.Queue()

    def initworker(self):
        pass
    def connections(self):
        self.qt_AES_btn.clicked.connect()
#done
    def save_binary(self,text):
        path,_=QFileDialog.getSaveFileName( None, "Open Bin File", "./", "Binary Files (*.bin)")
        with open(path, 'wb+') as f:
            f.write(text)
            
    def read_binary(self):
        binary=None
        path,_=QFileDialog.getOpenFileName( None, "Open Bin File", "./", "Binary Files (*.bin)")
        with  open(path, 'rb') as f:
            binary=f.read()
        return binary
        


    def findchildreen(self):
        self.qt_keysizeComboBox = self.window.findChild(QComboBox, "KeySizeComboBox")
        self.qt_cipher = self.window.findChild(QTextEdit, "CipherArea")
        self.qt_text = self.window.findChild(QTextEdit, "TextArea")        
        self.qt_key_line = self.window.findChild(QLineEdit, "Key_lineEdit")

        self.qt_AES_btn = self.window.findChild(QPushButton, "AES_btn")
        self.qt_AES_Dbtn = self.window.findChild(QPushButton, "AES_Dbtn")
        
        self.qt_DES_btn = self.window.findChild(QPushButton, "DES_btn")
        self.qt_DES_Dbtn = self.window.findChild(QPushButton, "DES_Dbtn")
       
        self.qt_ECC_btn = self.window.findChild(QPushButton, "ECC_btn")
        self.qt_ECC_Dbtn = self.window.findChild(QPushButton, "ECC_Dbtn")
        
        self.qt_MD5_btn = self.window.findChild(QPushButton, "MD5_btn")
        
        self.qt_SHA256_btn = self.window.findChild(QPushButton, "SHA256_btn")
        
        self.qt_RSA_btn = self.window.findChild(QPushButton, "RSA_btn")
        self.qt_RSA_Dbtn = self.window.findChild(QPushButton, "RSA_Dbtn")
        
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
        self.qt_DES_btn.clicked.connect(self.DES_Encrypt)
        self.qt_DES_Dbtn.clicked.connect(self.DES_Decrypt)
        self.qt_RSA_btn.clicked.connect(self.RSA_Encrypt)
        self.qt_RSA_Dbtn.clicked.connect(self.RSA_Decrypt)
        self.qt_SHA256_btn.clicked.connect(self.hash_sha256)
        self.qt_MD5_btn.clicked.connect(self.hash_md5)
        self.qt_ECC_btn.clicked.connect(self.ECC_Encrypt)
        self.qt_ECC_Dbtn.clicked.connect(self.ECC_Decrypt)
        
        



def main():
    app = QApplication(sys.argv)
    window = MainUI()
    app.exec()


if __name__ == "__main__":
    main()

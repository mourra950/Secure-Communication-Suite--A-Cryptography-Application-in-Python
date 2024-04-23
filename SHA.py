# import random
# import sys
# import time
# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes
# import queue
# import math
from PySide6.QtCore import (
    QObject,
    QRunnable,
    Slot,
)
# from PySide6.QtWidgets import (
#     QApplication,
#     QLabel,
#     QMainWindow,
#     QPushButton,
#     QVBoxLayout,
#     QWidget,
# )
import hashlib
class SHA256_Task():


    def __init__(self): #,plaintext_queue,ciphertext_queue,data
        super().__init__()
        # self.data=data
        # print(self.data.test)
        # self.plaintext_queue=plaintext_queue
        # self.ciphertext_queue=ciphertext_queue
        # self.hasher = hashlib.new("SHA256")
    def hash_sha256(self):
        hasher = hashlib.new("SHA256")
        plaintext=self.qt_text.toPlainText()
        hasher.update(plaintext.encode())
        self.qt_cipher.setText(str(hasher.hexdigest()))
    
        
        # print("output",self.hasher.hexdigest())

    # @Slot()
    # def run(self):
    #     """
    #             Initialize the runner function with passed self.args,
    #     self.kwargs.
    #     """
    #     counter =0
    #     print("run")
    #     while True:
    #         plaintext = self.plaintext_queue.get()
    #         counter += 1
    #         if plaintext is None:
    #             counter += 1
    #             break
    #         tmptext = f'{plaintext}'

    #         tmptext = tmptext.encode()
    #         self.hasher.update(tmptext)
    #         print("output",self.hasher.hexdigest())
            
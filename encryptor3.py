import random
import sys
import time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import queue
import math
from PySide6.QtCore import (
    QObject,
    QRunnable,
    QThreadPool,
    QTimer,
    Signal,
    Slot,
)
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
import rsa
class EncryptionWorker3(QRunnable):


    def __init__(self,plaintext_queue,ciphertext_queue,data):
        super().__init__()
        self.data=data
        print(self.data.test)
        self.plaintext_queue=plaintext_queue
        self.ciphertext_queue=ciphertext_queue
        self.public_key,self.private_key = rsa.newkeys(1024)
        

    @Slot()
    def run(self):
        """
                Initialize the runner function with passed self.args,
        self.kwargs.
        """
        counter =0
        print("run")
        while True:
            plaintext = self.plaintext_queue.get()
            counter += 1
            if plaintext is None:
                counter += 1
                break
            tmptext = f'{plaintext}'

            tmptext = tmptext.encode()
            ciphertext = rsa.encrypt(tmptext,self.public_key)

            outtext = rsa.decrypt(ciphertext, self.private_key)
            
            outtext = outtext.decode()
            
            self.ciphertext_queue.put(ciphertext)
            print(counter,tmptext,ciphertext)
            print("output",outtext)
            
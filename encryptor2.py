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
from Crypto.Util.Padding import pad,unpad



class EncryptionWorker2(QRunnable):
    """
    Worker thread

    :param args: Arguments to make available to the run code
    :param kwargs: Keywords arguments to make available to the run
    :code
    :
    """

    def __init__(self,plaintext_queue,ciphertext_queue,data):
        super().__init__()
        self.data=data
        print(self.data.test)
        self.plaintext_queue=plaintext_queue
        self.ciphertext_queue=ciphertext_queue
        self.key = get_random_bytes(self.data.keysize)
        
        # self.keysize=16
        self.AES_setup()

    def AES_setup(self):
        self.cipher = AES.new(self.key, AES.MODE_EAX)

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
            self.AES_setup()
            tmptext = f'{plaintext}'

            tmptext = bytes(tmptext, 'utf-8')
            tmptext = pad(tmptext,self.cipher.block_size)

            ciphertext = self.cipher.encrypt(tmptext)
            # self.cipher.update()
            
            self.cipher2 = AES.new(self.key, AES.MODE_EAX)

            outtext = unpad(self.cipher2.decrypt(ciphertext),self.cipher.block_size)
            
            
            
            self.ciphertext_queue.put(bytes(ciphertext))
            print(counter,tmptext,ciphertext)
            print("keysize",self.data.keysize)
            print("output",outtext)
            

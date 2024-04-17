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


class EncryptionWorker2(QRunnable):
    """
    Worker thread

    :param args: Arguments to make available to the run code
    :param kwargs: Keywords arguments to make available to the run
    :code
    :
    """

    def __init__(self,plaintext_queue,ciphertext_queue):
        super().__init__()
        self.plaintext_queue=plaintext_queue
        self.ciphertext_queue=ciphertext_queue
        self.keysize=16
        self.AES_setup()

    def AES_setup(self):
        self.key = get_random_bytes(self.keysize)
        self.cipher = AES.new(self.key, AES.MODE_EAX)

    def padding(self, message):
        # padding message
        len_diff = self.keysize - len(message)
        if (math.copysign(1, len_diff) == 1):
            message += b"\0"*len_diff
            return message
        else:
            return b"too long"

    @Slot()
    def run(self):
        """
                Initialize the runner function with passed self.args,
        self.kwargs.
        """
        print("run")
        while True:
            plaintext = self.plaintext_queue.get()
            if plaintext is None:
                counter += 1
                break
            tmptext = f'{plaintext}'

            tmptext = bytes(tmptext, 'utf-8')
            tmptext = self.padding(tmptext)
            print(tmptext)

            ciphertext = self.cipher.encrypt(tmptext)
            self.ciphertext_queue.put(bytes(ciphertext))
            print(ciphertext)

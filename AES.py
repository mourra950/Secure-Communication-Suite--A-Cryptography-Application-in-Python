from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

from PySide6.QtWidgets import QFileDialog


class AES_Task():
    def __init__(self):
        super().__init__()
        self.keysize = 16

    def AES_Encrypt(self, toggle=False,text="ahmed"):
        plaintext = text
        # plaintext = self.qt_text.toPlainText()

        # AES key must be either 16, 24, or 32 bytes long

        self.key_AES = get_random_bytes(self.keysize)
        cipher = AES.new(self.key_AES, AES.MODE_EAX, nonce=b'1'*16)
        self.blockSize_AES = cipher.block_size
        print(f"Block size: {self.blockSize_AES}")
        print(f"plaintext: {text}")
        bytesplaintext = bytes(plaintext, 'utf-8')
        padedtext = pad(bytesplaintext, cipher.block_size, style='iso7816')
        ciphertext = cipher.encrypt(padedtext)

        return ciphertext, self.key_AES

    def AES_Decrypt(self, ciphertext, key_AES):
        print(f"key_AES: {key_AES}")
        Decipher = AES.new(key_AES, AES.MODE_EAX, nonce=b'1'*16)
        decryptedtext = unpad(Decipher.decrypt(
            ciphertext), 16, style='iso7816')
        return decryptedtext.decode('utf-8')

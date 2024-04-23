from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

from PySide6.QtWidgets import  QFileDialog
class AES_Task():
    def __init__(self):
        super().__init__()

    def AES_Encrypt(self):
        plaintext = self.qt_text.toPlainText()
        # AES key must be either 16, 24, or 32 bytes long

        self.key_AES = get_random_bytes(self.keysize)
        cipher = AES.new(self.key_AES, AES.MODE_EAX, nonce=b'1'*16)
        self.blockSize_AES = cipher.block_size

        bytesplaintext = bytes(plaintext, 'utf-8')
        padedtext = pad(bytesplaintext, cipher.block_size, style='iso7816')
        ciphertext = cipher.encrypt(padedtext)
        path,_=QFileDialog.getSaveFileName( None, "Open Bin File", "./", "Binary Files (*.bin)")
        with open(path, 'wb+') as f:
            f.write(ciphertext)
        self.qt_cipher.setText(str(ciphertext))

    def AES_Decrypt(self):
        path,_=QFileDialog.getOpenFileName( None, "Open Bin File", "./", "Binary Files (*.bin)")
        with  open(path, 'rb') as f:
            ciphertext=f.read()
            
        Decipher = AES.new(self.key_AES, AES.MODE_EAX, nonce=b'1'*16)
        decryptedtext = unpad(Decipher.decrypt(
            ciphertext), self.blockSize_AES, style='iso7816')
        self.qt_cipher.setText("Message when Decrypted: " +
                               decryptedtext.decode("utf-8"))
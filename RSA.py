import rsa
from Crypto.PublicKey import ECC


class RSA_Task():

    def __init__(self):  # ,plaintext_queue,ciphertext_queue,data
        super().__init__()
        self.public_key, self.private_key = rsa.newkeys(1024)

    def RSA_Encrypt(self):
        plaintext = self.qt_text.toPlainText()
        ciphertext = rsa.encrypt(plaintext.encode(), self.public_key)
        self.save_binary(ciphertext)
        self.qt_cipher.setText(str(ciphertext))

    def RSA_Decrypt(self):
        plaintext = self.read_binary()
        outtext = rsa.decrypt(plaintext, self.private_key)
        outtext = outtext.decode()
        self.qt_cipher.setText("Decrypted RSA is '"+outtext+"'")

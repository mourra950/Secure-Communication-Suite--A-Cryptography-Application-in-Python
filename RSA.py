import rsa
from Crypto.PublicKey import ECC


class RSA_Task():

    def __init__(self):  # ,plaintext_queue,ciphertext_queue,data
        super().__init__()
        self.rsa_public_key, self.rsa_private_key = rsa.newkeys(256)

    def RSA_Encrypt(self, private, public, text):
        plaintext = text
        ciphertext = rsa.encrypt(plaintext.encode(), public)
        ciphertext = rsa.encrypt(ciphertext, private)
        return ciphertext
        # self.save_binary(ciphertext)
        # self.qt_cipher.setText(str(ciphertext))

    def RSA_Decrypt(self, private, public, text):
        plaintext = text
        outtext = rsa.decrypt(plaintext, private)
        outtext = rsa.decrypt(outtext, public)
        outtext = outtext.decode()
        return f"{outtext}"
        # self.qt_cipher.setText("Decrypted RSA is '"+outtext+"'")

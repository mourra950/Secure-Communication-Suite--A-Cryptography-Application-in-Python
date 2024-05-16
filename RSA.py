import rsa
from Crypto.PublicKey import ECC
from Crypto.Util.Padding import pad, unpad


class RSA_Task():

    def __init__(self):  # ,plaintext_queue,ciphertext_queue,data
        super().__init__()
        self.rsa_public_key, self.rsa_private_key = rsa.newkeys(1024)
        print(self.rsa_public_key)

    def RSA_Encrypt(self, private, public, text):
        plaintext_bin =  text
        
        ciphertext = rsa.encrypt(plaintext_bin, public)
        
        # print(private,ciphertext,len(ciphertext))
        
        # ciphertext = rsa.encrypt(ciphertext, private)
        return ciphertext
        # self.save_binary(ciphertext)
        # self.qt_cipher.setText(str(ciphertext))

    def RSA_Decrypt(self, private, text):
        plaintext = text
        outtext = rsa.decrypt(plaintext, private)
        # outtext = rsa.decrypt(outtext, public)
        print(outtext)
        # outtext = outtext.decode()
        return outtext
        # self.qt_cipher.setText("Decrypted RSA is '"+outtext+"'")

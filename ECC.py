from Crypto.PublicKey import ECC
from ecies.utils import generate_eth_key
from ecies import encrypt, decrypt
from PySide6.QtWidgets import  QFileDialog
import binascii
class ECC_Task():

    def __init__(self):#,plaintext_queue,ciphertext_queue,data
        super().__init__()
        self.private_key = generate_eth_key()
        self.private_key_hex = self.private_key.to_hex()
        self.public_key_hex = self.private_key.public_key.to_hex()

    
    def ECC_Encrypt(self):
        plaintext=self.qt_text.toPlainText().encode()
        ciphertext = encrypt(self.public_key_hex, plaintext)
        self.save_binary(ciphertext)
        self.qt_cipher.setText(str(ciphertext))
        
    def ECC_Decrypt(self):
        ciphertext = self.read_binary()
        decryptedtext = decrypt(self.private_key_hex , ciphertext)

        self.qt_cipher.setText("Message when Decrypted: " +
                               decryptedtext.decode("utf-8"))
            
    #         self.ciphertext_queue.put(ciphertext)
    #         print(counter,tmptext,ciphertext)

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
    #         ciphertext = rsa.encrypt(tmptext,self.public_key)

    #         outtext = rsa.decrypt(ciphertext, self.private_key)
            
    #         outtext = outtext.decode()
            
    #         self.ciphertext_queue.put(ciphertext)
    #         print(counter,tmptext,ciphertext)
    #         print("output",outtext)
            
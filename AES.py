from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PySide6.QtCore import (
    Slot,
)

from Crypto.Util.Padding import pad,unpad



class AES_Task():
    def __init__(self):
        super().__init__()
        
        

    def AES_Encrypt(self):
        plaintext=self.qt_text.toPlainText()
        self.key_AES = get_random_bytes(self.keysize)
        cipher = AES.new(self.key_AES, AES.MODE_EAX,nonce=b'1'*16)
        self.blockSize_AES=cipher.block_size
        
        bytesplaintext = bytes(plaintext, 'utf-8')
        padedtext = pad(bytesplaintext,cipher.block_size,style='iso7816')
        ciphertext = cipher.encrypt(padedtext)
        self.encrypted=ciphertext
        self.qt_cipher.setText(str(ciphertext))
        
    def AES_Decrypt(self):
        ciphertext=self.encrypted
        # ciphertext = bytes(ciphertext, 'utf-8')
        # ciphertext =pad(ciphertext,self.blockSize_AES,style='iso7816')
        
        Decipher=AES.new(self.key_AES, AES.MODE_EAX,nonce=b'1'*16)
        decryptedtext=unpad(Decipher.decrypt(ciphertext),self.blockSize_AES,style='iso7816')
        self.qt_cipher.setText("Message when Decrypted "+ decryptedtext.decode("utf-8"))
        
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
    #         self.AES_setup()
    #         tmptext = f'{plaintext}'

    #         tmptext = bytes(tmptext, 'utf-8')
    #         tmptext = pad(tmptext,self.cipher.block_size,style='iso7816')

    #         ciphertext = self.cipher.encrypt(tmptext)
    #         # self.cipher.update()
    #         print("NOnceeeee",self.cipher.nonce)
    #         self.cipher2 = AES.new(self.key, AES.MODE_EAX,nonce=b'1'*16)

    #         outtext = unpad(self.cipher2.decrypt(ciphertext),self.cipher.block_size,style='iso7816')
            
            
            
    #         self.ciphertext_queue.put(bytes(ciphertext))
    #         print(counter,tmptext,ciphertext)
    #         print("keysize",self.data.keysize)
    #         print("output",outtext)
            

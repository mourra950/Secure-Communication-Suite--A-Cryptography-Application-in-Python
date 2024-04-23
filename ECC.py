from Crypto.PublicKey import ECC

class ECC_Task():


    def __init__(self):#,plaintext_queue,ciphertext_queue,data
        super().__init__()
        # self.data=data
        # print(self.data.test)
        # self.plaintext_queue=plaintext_queue
        # self.ciphertext_queue=ciphertext_queue
        self.public_key,self.private_key = rsa.newkeys(1024)
    
    def RSA_Encrypt(self):
        plaintext=self.qt_text.toPlainText()
        ciphertext = rsa.encrypt(plaintext.encode(),self.public_key)
        self.RSA_ciphertext=ciphertext
        self.qt_cipher.setText(str(ciphertext))
        
    def RSA_Decrypt(self):
        plaintext=self.RSA_ciphertext
        outtext = rsa.decrypt(plaintext, self.private_key)
        outtext = outtext.decode()
        self.qt_cipher.setText("Decrypted RSA is '"+outtext+"'")
        
            
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
            
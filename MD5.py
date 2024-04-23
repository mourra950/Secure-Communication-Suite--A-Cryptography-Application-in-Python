import hashlib
class MD5_Task():


    def __init__(self): #,plaintext_queue,ciphertext_queue,data
        super().__init__()
    def hash_md5(self):
        hasher = hashlib.new("md5")
        plaintext=self.qt_text.toPlainText()
        hasher.update(plaintext.encode())
        self.qt_cipher.setText(str(hasher.hexdigest()))
    
        
 
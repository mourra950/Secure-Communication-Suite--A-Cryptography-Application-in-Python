import hashlib
class SHA256_Task():

    def __init__(self): #,plaintext_queue,ciphertext_queue,data
        super().__init__()
    def hash_sha256(self):
        hasher = hashlib.new("SHA256")
        plaintext=self.qt_text.toPlainText()
        hasher.update(plaintext.encode())
        self.qt_cipher.setText(str(hasher.hexdigest()))
        return str(hasher.hexdigest())
    
import hashlib

def hash_sha256(self,text):
    hasher = hashlib.new("SHA256")
    plaintext=text.toPlainText()
    hasher.update(plaintext.encode())
    return str(hasher.hexdigest())
    
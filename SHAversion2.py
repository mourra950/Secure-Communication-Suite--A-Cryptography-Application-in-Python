import hashlib

def hash_sha256(text):
    hasher = hashlib.new("SHA256")
    plaintext=text
    hasher.update(plaintext.encode())
    return str(hasher.hexdigest())
    
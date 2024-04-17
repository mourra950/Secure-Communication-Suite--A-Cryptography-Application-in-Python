import threading
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import queue
import math

class EncryptionWorker(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
        self.keysize = 32
        # AES key must be either 16, 24, or 32 bytes long
        self.AES_setup()
        print("init")
    def AES_setup(self):
        self.key = get_random_bytes(self.keysize)
        self.cipher = AES.new(self.key, AES.MODE_EAX)
    def padding(self, message):
        # padding message
        len_diff = self.keysize - len(message)
        if( math.copysign(1,len_diff)==1):
            message += b"\0"*len_diff
            return message
        else:
            return b"too long"
            

    def run(self):
        print("run")
        while True:
            plaintext = self.plaintext_queue.get()

            if plaintext is None:
                counter += 1
                break
            tmptext = f'{plaintext}'
            
            tmptext = bytes(tmptext, 'utf-8')
            tmptext=self.padding(tmptext)
            print(tmptext)
            
            ciphertext = self.cipher.encrypt(tmptext)
            self.ciphertext_queue.put(bytes(ciphertext))
            print(ciphertext)


def main():
    plaintext_queue = queue.Queue()
    ciphertext_queue = queue.Queue()
    print("hamda")
    worker = EncryptionWorker(plaintext_queue, ciphertext_queue)
    worker.start()
    worker.join()

if __name__=="__main__":
    main()

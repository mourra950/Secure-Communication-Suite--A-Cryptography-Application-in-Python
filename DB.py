from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
URI = "mongodb+srv://omarelbanna:AtieyhIE9Xj2wCKk@security.yxz4gwr.mongodb.net/?retryWrites=true&w=majority&appName=security"
class DB:
    def __init__(self):
        print("Connecting...")
        self.client = MongoClient(URI, server_api=ServerApi('1'))
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

        self.db = self.client["Security"]
        self.users = self.db["Users"]
        self.keys= self.db["Keys"]

        
    





# from pymongo import MongoClient

# mongo_db_url = "mongodb+srv://magan:1234@cluster0.j2rs4.mongodb.net/?retryWrites=true&w=majority"
# try:
#     client = MongoClient(mongo_db_url, tls=True, tlsAllowInvalidCertificates=True)
#     print(client.list_database_names())
# except Exception as e:
#     print("Connection failed:", e)


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://magan:1234@cluster0.j2rs4.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



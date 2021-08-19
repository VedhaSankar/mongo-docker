import pymongo
from pymongo import MongoClient
# import pymongo.errors as pymon_err
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI')

# creating a MongoClient object  
client = MongoClient(MONGO_URI)  

# accessing the database  
DB_NAME = 'trials'
database = client[DB_NAME]



def insert_records():

    result = {

        "result"    : "1"

    }

    collection_name = 'docker'
    new_collection = database[collection_name]

    x = new_collection.insert_one(result)
    print(x)


def startpy():

    insert_records()


if __name__ == '__main__':

    startpy()


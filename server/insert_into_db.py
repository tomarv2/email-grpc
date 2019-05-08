# Create MongoDB database
import pymongo
import yaml_parser

client = pymongo.MongoClient(yaml_parser.mongodb_out('mongodb_url'))

def insert_db(dbname, cust_info):
    db = client[dbname]
    collection = db.user_details
    try:
        collection.insert_one(cust_info)
    except:
        pass


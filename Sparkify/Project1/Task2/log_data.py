import pymongo
import json
import os

client = pymongo.MongoClient('localhost', 27017)
db = client.log_db
week1 = db.log_col1
week2 = db.log_col2
week3 = db.log_col3
week4 = db.log_col4


for file in os.listdir('./'):
    if file.endswith(".json"):
        name = str(file)
        date = int(name[8:10])
        if 0<date<=7:
            with open(file,'r') as f:
                for line in f:
                    obj = json.loads(line)
                    db.week1.insert_one(obj)

        elif 7<date<=14:
            with open(file,'r') as f:
                for line in f:
                    obj = json.loads(line)
                    db.week2.insert_one(obj)

        elif 14<date<=21:
            with open(file,'r') as f:
                for line in f:
                    obj = json.loads(line)
                    db.week3.insert_one(obj)
        else:
            with open(file,'r') as f:
                for line in f:
                    obj = json.loads(line)
                    db.week4.insert_one(obj)
from flask import render_template
import pymongo
from pymongo import MongoClient
from flask import Flask


client = MongoClient ('localhost', 27017)
db = client['log_db']
log = db['coll']

app = Flask(__name__)

@app.route("/")

def top10():
    sw1 = list(db.week1.aggregate([{"$unwind": "$song"}, {"$sortByCount": "$song"}, { "$limit" : 10 }]))
    aw1 = list(db.week1.aggregate([{"$unwind": "$artist"}, {"$sortByCount": "$artist"}, { "$limit" : 10 }]))
    sw2 = list(db.week2.aggregate([{"$unwind": "$song"}, {"$sortByCount": "$song"}, { "$limit" : 10 }]))
    aw2 = list(db.week2.aggregate([{"$unwind": "$artist"}, {"$sortByCount": "$artist"}, { "$limit" : 10 }]))
    sw3 = list(db.week3.aggregate([{"$unwind": "$song"}, {"$sortByCount": "$song"}, { "$limit" : 10 }]))
    aw3 = list(db.week3.aggregate([{"$unwind": "$artist"}, {"$sortByCount": "$artist"}, { "$limit" : 10 }]))
    sw4 = list(db.week4.aggregate([{"$unwind": "$song"}, {"$sortByCount": "$song"}, { "$limit" : 10 }]))
    aw4 = list(db.week4.aggregate([{"$unwind": "$artist"}, {"$sortByCount": "$artist"}, { "$limit" : 10 }]))
    temp = sw1 + aw1 +sw2 + aw2+ sw3 + aw3 +sw4 + aw4
    with app.app_context(), app.test_request_context():
            template = render_template('index.html',temp=temp)
    return template

top10()
from flask import render_template
from flask import Flask
import psycopg2

#connecting to database
conn = psycopg2.connect(database="postgres", user="postgres", password="4m5EVwdUBLv5Z8l0dCPR",host="sparkifyrds.cw8bzocbnw3p.us-east-1.rds.amazonaws.com",port="5432")

cur=conn.cursor()

app = Flask(__name__)                                                                                                   
@app.route("/")

def top10():                                                                                                            
    cur.execute("SELECT status->>'song' FROM raw_events where status->>'week' = '1' group by status->>'song' order by COUNT(status->>'song') desc limit 10;")
    sw1 = list(cur.fetchall())

    cur.execute("SELECT status->>'artist' FROM raw_events where status->>'week' = '1' group by status->>'artist' order by COUNT(status->>'artist') desc limit 10;")
    aw1 = list(cur.fetchall())


    cur.execute("SELECT status->>'song' FROM raw_events where status->>'week' = '2' group by status->>'song' order by COUNT(status->>'song') desc limit 10;")
    sw2 = list(cur.fetchall())


    cur.execute("SELECT status->>'artist' FROM raw_events where status->>'week' = '2' group by status->>'artist' order by COUNT(status->>'artist') desc limit 10;")                                                                                 aw2 = list(cur.fetchall())


    cur.execute("SELECT status->>'song' FROM raw_events where status->>'week' = '3' group by status->>'song' order by COUNT(status->>'song') desc limit 10;")
    sw3 = list(cur.fetchall())


    cur.execute("SELECT status->>'artist' FROM raw_events where status->>'week' = '3' group by status->>'artist' order by COUNT(status->>'artist') desc limit 10;")
    aw3 = list(cur.fetchall())

    cur.execute("SELECT status->>'song' FROM raw_events where status->>'week' = '4' group by status->>'song' order by COUNT(status->>'song') desc limit 10;")
    sw4 = list(cur.fetchall())                                                                                          
    cur.execute("SELECT status->>'artist' FROM raw_events where status->>'week' = '4' group by status->>'artist' order by COUNT(status->>'artist') desc limit 10;")
    aw4 = list(cur.fetchall())                                                                                          
    temp = sw1 + aw1 +sw2 + aw2+ sw3 + aw3 +sw4 + aw4
    with app.app_context(), app.test_request_context():
        template = render_template('pg.html',temp=temp)
    return template 

top10()
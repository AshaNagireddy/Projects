'''
Instructions:
1. ssh to master node 
	ssh -i C:/Users/ashan/Downloads/sparkey.pem hadoop@ec2-54-91-19-200.compute-1.amazonaws.com
2. unset PYSPARK_DRIVER_PYTHON
3. creating python script file
	vi spark7.py
4. spark-submit spark7.py	

'''

import sys
import json
from pyspark import SparkContext, SparkConf

if __name__ == "__main__":

  # create Spark context with Spark configuration
    conf = SparkConf().setAppName("Top-20").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    data = sc.textFile("s3a://anagi1project6/*.json")
    files=data.collect()

out = []
song_dict = {}
songs = []
for line in files:
    line = json.loads(line)
    temp = line['song']
    if temp!=None:
        if temp not in song_dict:
            song_dict[temp] = 1
        else: song_dict[temp] += 1


for key, value in song_dict.items():
    songs.append([key, value])


#sorting in descending order
songs = sorted(songs, key = lambda x:x[1],reverse = True)

#creating out put string..
outlst = ""
for i in songs[:20]:
    outlst += i[0] + '\n'

print(outlst.encode('utf-8'))

sc.parallelize(outlst).saveAsTextFile("s3a://anagi1-spark7/output")
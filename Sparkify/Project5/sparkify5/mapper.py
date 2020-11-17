import json
import sys

out = []

for line in sys.stdin:
    line = json.loads(line)
    artist = line['artist']
    song = line['song']
    if artist!= None:
        out.append(["A",artist,1])
    if song!=None:
        out.append(["S",song,1])
print(out)
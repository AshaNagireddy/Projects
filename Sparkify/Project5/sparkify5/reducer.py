import sys
art_dict = {}
song_dict = {}

for i in list(sys.stdin):
    if i[0] == "A":
        if i[1] not in art_dict:
            art_dict[i[1]] = 1
        else: art_dict[i[1]] += 1
    else:    
        if i[1] not in song_dict:
            song_dict[i[1]] = 1
        else: song_dict[i[1]] += 1
            
for key, value in song_dict.items():
    song.append([key, value])

for key, value in art_dict.items():
    artist.append([key, value])


song = sorted(song, key = lambda x:x[1],reverse = True)
artist = sorted(artist, key = lambda x:x[1],reverse = True)
print("top 10 songs\n")
for i in range(10):
    print(song[i][0], song[i][1]) 
print("\ntop 10 artists\n")
for i in range(10):
    print(artist[i][0], artist[i][1])
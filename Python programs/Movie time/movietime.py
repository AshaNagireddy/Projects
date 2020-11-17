'''
Author: Asha Nagireddy
Code: movie time
version: 1
Date: 17th December 2019
'''
import sys
#function to validate inputs
def validate(genre,rating,merge_list):
    final_list = []
    for n in merge_list:
        if (n[1] == rating) and (n[2] == genre): #matching inputs..
            final_list.append([n[0],n[3]])   #creating matched list..
    return final_list

#function to extract data from 2 files..
def extract(x,s):
    filename = 'C:/Users/ashan/Desktop/Asha_masters/python/Finals/' + x
    file = open(filename,'r',encoding="utf8")    #encoding="utf8" to remove error in IDE
    data = file.readlines()
    file.close()
    data_dic={}
    for i in data:
        i.strip("\n")  #stripping out special characters
        line = i.split(s) #splitting lines in files into list
        line[1] = int(line[1])
        line[2] = float(line[2])
        data_dic[line[1]] = [line[0],line[2]] #creating dictionary with movie id as key and list of rating/genre and ranking as values..
    return data_dic

#main function....
def main():
    #Reading and retrieving data from imdb.txt file
    data1_dic = extract("imdb.txt"," ")
    #Reading and retrieving data from movielens.txt file
    data2_dic = extract("movielens.txt",",")

    #merging..
    data1_set = set(data1_dic.keys())
    data2_set = set(data2_dic.keys())
    merge_set = data1_set & data2_set #intersection command to extract common data
    merge_id = list(merge_set)

    #preparing common data list...
    merge_list = []
    for i in merge_id:
        temp1 = data1_dic[i]  #storing [rating,ranking] in variable
        temp2 = data2_dic[i]  #storing [genre,ranking] in variable
        avg_rank = ((temp1[1]*2)+temp2[1])/2  #calculating avg rank and rounding value
        avg_rank = round(avg_rank,2)
        merge_list.append([i,temp1[0],temp2[0],avg_rank])  #creating merged data list

    #sorting merged list with rank
    merge_list.sort(key=lambda x:x[3], reverse=True)  #sorting the list with rank in descending order
    
    return merge_list

# taking command line arguments...
genre = sys.argv[1]
rating = sys.argv[2]

#creating required data with common id in both files...
merge_list = main()

#validation...
final_list = validate(genre,rating,merge_list)
l = len(final_list)

if l == 0: #input data failed validation..
    print("Invalid input")  #error message and quit...
    sys.exit()
else: #validation passed
    print("------------------------")
    print("|Movie id  |  Ranking  |")
    print("------------------------")
    if l > 10: #printing top 10 ranks
        l = 10
    for i in range(l):
        print("|  {0} \t   |\t {1}  |".format(final_list[i][0],final_list[i][1]))  #displaying result...
        print("------------------------")

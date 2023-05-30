import glob
import pandas as pd

# Get data file names
path = r'F:\SGIPC\indiv\players'
filenames = glob.glob(path + "/*.csv")

import csv
from os import read

all_data = []
f = open('indiv/nameOnly.csv', 'w')

def func(file_name, username):
    with open(file_name, "r" )as f:
        reader = csv.reader(f)
        #next(reader)
        data = []
        for i in range(0,7):
            data.append({
                "contest_id":"",
                "rating":"",
                "place":"",
            })
        i = 0 
        for row in reader:
            if(row[0]=='contest_index'):
                continue
            i = int(row[0])
            #print(i)
            data[i] = {
                "contest_id":row[0],
                "rating":row[1],
                "place":row[4]
            }
            #print(data[i], row[0])
        
        #with open(glob.glob(path + "new_.csv"), "w" )as f:
        #f = open('indiv/new_.csv', 'w')
        
        
        
        #data = ['Afghanistan', 652090, 'AF', 'AFG']

        
        p = []
        for i in range(17):
            p.append("-")
        p[0] = username
        # write the data
        i = 1
        lastid= -1
        last = 0
        cnt = 0
        for d in data:
            if(d['contest_id']==""):
                continue
            id = int(d['contest_id'])
            place = d['place']
            rating = d['rating']
            
            id = 2*id+1
            p[id]= int(rating)
            p[id+1] = place
            cnt+=1
            
            if(id>lastid):
                last = int(rating)
        p[15] = int(last)+cnt*30
        p[16] = cnt

        all_data.append(p)
            #writer.writerow(p)



            

dfs = []
f=0
for filename in filenames:
    #print(filename)
    s=filename
    
    s = s[23:-4]
    if(f<=0):
        func(filename,s)
        
    #print(s)

#

#all_data = sorted(all_data, key = lambda x: (-x[15], x[0]))
header = ['Rank','Name', '0','0-rank', '1','1-rank', '2','2-rank','3','3-rank', '4','4-rank', '5','5-rank','6','6-rank','Rating','Count']
with open('indiv/new_.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)

            # write the header
            #writer.writerow(header)
            
            
            
            # k = 1
            for i in all_data:
                j = []
                j.append(i[0])
                # k+=1
                # for r in i:
                #     j.append(r)
                writer.writerow(j)
    
    
    #dfs.append(pd.read_csv(filename))

# Concatenate all data into one DataFrame
#big_frame = pd.concat(dfs, ignore_index=True)
#sob plot run korlei paoa jabe. jesob team ekta contest koreche tader point dekha jabe just. 
#csv to html page create korle, just proti team er sathe linked kore plot upload dilei hobe.


import pandas as pd
import matplotlib.pyplot as plt


lis = {}

ruet1 = pd.read_csv (r'ruet1.csv')
ruet2 = pd.read_csv (r'ruet2.csv')
ruet3 = pd.read_csv (r'ruet3.csv')
colab = pd.read_csv (r'colab.csv')



df = pd.DataFrame()  
cnt=0
for i in ruet1:
    lis[ruet1['handle'][cnt]] = [ruet1['display_rating'][cnt]]
    cnt +=1


cnt=0
for i in ruet2:
    lis[ruet2['handle'][cnt]].append(ruet2['display_rating'][cnt])
    cnt +=1

cnt=0
for i in ruet3:
    lis[ruet3['handle'][cnt]].append(ruet3['display_rating'][cnt])
    cnt +=1


cnt=0
for i in colab['handle']:
    #print(colab['handle'][cnt])
    if colab['handle'][cnt] in lis: 
        lis[colab['handle'][cnt]].append(colab['display_rating'][cnt])
    else: 
        lis[colab['handle'][cnt]] = [colab['display_rating'][cnt]]
    cnt +=1


for i in lis:
    #print(i)
    for x in range(4-len(lis[i])):
        lis[i].append(None)
        
df = pd.DataFrame.from_dict(lis)

for i in lis:
    df[i].plot(x ='contest_no', y='rating', kind = 'line')
    plt.show()


























import json
import csv
from os import read


handle = []

with open("ruet1.csv", "r" )as f:
    reader = csv.reader(f)
    #next(reader)
    for row in reader:
        handle.append(row[1])


ruet1 = []
ruet2 = []
ruet3 = []
colab26 = []
colab27 = []

with open("ruet1.csv", "r" )as f:
    reader = csv.reader(f)
    #next(reader)
    for row in reader:
        for j in handle:
            if(j==row[1]):
                ruet1.append(row[2])
                break
with open("ruet2.csv", "r" )as f:
    reader = csv.reader(f)
    #next(reader)
    for row in reader:
        f = 0
        for j in handle:
            if(j==row[1]):
                ruet2.append(row[2])
                f=1
                break
            
with open("ruet3.csv", "r" )as f:
    reader = csv.reader(f)
    #next(reader)
    for row in reader:
        for j in handle:
            if(j==row[1]):
                ruet3.append(row[2])
                break

with open("colab26.csv", "r" )as f:
    reader = csv.reader(f)
    #next(reader)
    for row in reader:
        for j in handle:
            if(j==row[1]):
                colab26.append(row[2])
                break

with open("colab27.csv", "r" )as f:
    reader = csv.reader(f)
    #next(reader)
    for row in reader:
        for j in handle:
            if(j==row[1]):
                colab27.append(row[2])
                break





with open("current_all_together_rating.csv", "r" )as f:
    reader = csv.reader(f)
    #next(reader)
    data = []
    for row in reader:
        data.append({
            "handle":row[0],
            "1":row[1],
            "2":row[2],
            "3":row[3],
            "4":row[4]
        })

with open("current_all_together_rating.json", "w") as f:
    json.dump(data, f, indent=4)
import json
import csv
from os import read

with open("current_all_together_rating.csv", "r" )as f:
    reader = csv.reader(f)
    #next(reader)
    data = []
    for row in reader:
        data.append({
            "handle":row[0],
            "1":row[2],
            "2":row[3],
            "3":row[4],
            "4":row[5],
            "5":row[6],
            "6":row[7],
            "team":row[1]
        })

with open("current_all_together_rating.json", "w") as f:
    json.dump(data, f, indent=4)
import json
import csv
from os import read

with open("colab28.csv", "r" )as f:
    reader = csv.reader(f)
    #next(reader)
    data = []
    for row in reader:
        data.append({
            "rank":row[0],
            "handle":row[5],
            "rating":row[1],
            "contest_count":row[2],
            "rating_change":row[4],
            "last_contest": row[3]
        })

with open("colab28.json", "w") as f:
    json.dump(data, f, indent=4)
#Figures out the average stats per each weight class 
import pymongo
import csv
import sqlite3



#Setting Up The Connections To The DB
myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@octc1.d2he2mx.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]
nodatafighters = db["WEBFighterNoData"]
webeventdata = db["WEBFighterFights"]

#Filter Arguments For Each Weight Class
names = db.WEBFighterFights.distinct('fighterCode')

seen_names = set()

for doc in webeventdata.find():
    name = doc.get('fighterCode')
    if name in seen_names:
        print(f"Duplicate name found: {name}")
    else:
        seen_names.add(name)

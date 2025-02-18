#Figures out the average stats per each weight class 
import pymongo
import csv
import sqlite3



#Setting Up The Connections To The DB
myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@octc1.d2he2mx.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]
nodatafighters = db["WEBFighterNoData"]


#Filter Arguments For Each Weight Class
allinfonames = db.WEBFighterNoData.distinct('fighterURL')

for x in allinfonames:
    
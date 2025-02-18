#Figures out the average stats per each weight class 
import pymongo
import csv
import sqlite3



#Setting Up The Connections To The DB
myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@octc1.d2he2mx.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]
fighterdata = db["FighterData"]
fighternames = db["FighterNames"]
weightclasses = db["WeightClasses"]
wcav = db["WCAV"]
webfightdata = db["WEBFightData"]
webeventdata = db["WEBEventData"]


allfightset = set()
alleventset = set()

#Filter Arguments For Each Weight Class
alleventcodes = db.Events.distinct('eventCode')
allfightcodes = db.WEBFightData.distinct('fightCode')

for x in alleventcodes:
    xox = db.Events.find({"EventCode":x}, {"EventName":1, "_id":0}).distinct('EventName')
    eventName = xox[0]
    xox = db.Events.find({"EventCode":x}, {"Date":1, "_id":0}).distinct('Date')
    date = xox[0]
    
    mydict = { 
            "eventCode": x,
            "eventName": eventName,
            "date": date,
            "fight1"
            }
    
    webfightdata.insert_one(mydict)
    
    
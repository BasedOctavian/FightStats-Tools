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
webfightinfo = db["WEBFightInfo"]
webfighterinfo = db["WEBFighterInfo"]

#Filter Arguments For Each Weight Class
allinfonames = db.WEBFightInfo.distinct('BOUT')
allwebnames = db.WEBFightData.distinct('fightCode')


for x in allinfonames:
    
    #Gets The Fighter Names From The Info DB
    l = db.WEBFightInfo.find({"BOUT":x},{"BOUT":1,  "_id":0}).distinct('BOUT')
    boutName = l[0]
    fighters = boutName.split("vs.")
    fighter1 = fighters[0].strip()
    fighter2 = fighters[1].strip()
    
    #Get The Event Name From The DB
    
    
    
    for y in allwebnames:
        if x == y:
            myquery = { "FIGHTER": x }
            webfighterinfo.delete_one(myquery)
        


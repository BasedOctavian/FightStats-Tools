#Figures out the average stats per each weight class 
import pymongo
import csv
import sqlite3
from datetime import datetime



#Setting Up The Connections To The DB
myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@octc1.d2he2mx.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]
fighterdata = db["FighterData"]
fighternames = db["FighterNames"]
weightclasses = db["WeightClasses"]
wcav = db["WCAV"]
webfighterdata = db["WEBFighterData"]
webfighterinfo = db["WEBFighterInfo"]

#Filter Arguments For Each Weight Class
allinfonames = db.WEBFighterInfo.distinct('FIGHTER')
allwebnames = db.WEBFighterData.distinct('fighterName')

#Loops through all fighter info entries
for x in allinfonames:
    
    deleteit = False
    datefucked = False
    
    l = db.WEBFighterInfo.find({"FIGHTER":x},{"HEIGHT":1,  "_id":0}).distinct('HEIGHT')
    height = l[0]
    l = db.WEBFighterInfo.find({"FIGHTER":x},{"WEIGHT":1,  "_id":0}).distinct('WEIGHT')
    weight = l[0]
    l = db.WEBFighterInfo.find({"FIGHTER":x},{"REACH":1,  "_id":0}).distinct('REACH')
    reach = l[0]
    l = db.WEBFighterInfo.find({"FIGHTER":x},{"DOB":1,  "_id":0}).distinct('DOB')
    dob = l[0]
    
    if height and reach == "--":
        deleteit = True
    
    if height == "--":
        db.WEBFighterInfo.update_one({"FIGHTER":x}, {"$set": {"HEIGHT": "N/A"}})
        
    if weight == "--":
        db.WEBFighterInfo.update_one({"FIGHTER":x}, {"$set": {"WEIGHT": "N/A"}})
        
    if reach == "--":
        db.WEBFighterInfo.update_one({"FIGHTER":x}, {"$set": {"REACH": "N/A"}})
        
    if dob == "--":
        db.WEBFighterInfo.update_one({"FIGHTER":x}, {"$set": {"DOB": "N/A"}})
        datefucked = True
    
    
    #if datefucked == False:
       #date_string = dob
       #datetime_object = datetime.strptime(date_string, "%b %d, %Y")
       #formatted_date = datetime_object.strftime("%m/%d/%y")
       #db.WEBFighterInfo.update_one({"FIGHTER":x}, {"$set": {"DOB": formatted_date}})
    
    newurl = 'https://www.fightstats.xyz/fighterinfo/'
    
    l = db.WEBFighterInfo.find({"FIGHTER":x},{"FIGHTER":1,  "_id":0}).distinct('FIGHTER')
    name = l[0]
    lowercase_string = name.lower().replace(" ", "")
    newurl = newurl + lowercase_string
    
    newurl = "https://www.fightstats.xyz/search?q=" + name.lower()
    
    
    db.WEBFighterInfo.update_one({"FIGHTER":x}, {"$set": {"URL": newurl}})
    
    if deleteit == True:
        myquery = { "FIGHTER": x }
        webfighterinfo.delete_one(myquery)
   
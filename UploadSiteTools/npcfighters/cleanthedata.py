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
webfighterdata = db["WEBFighterData"]
webfighterinfo = db["WEBFighterNoData"]
webnodatadisplay = db["WEBNoDataDisplay"]

#Filter Arguments For Each Weight Class
allinfonames = db.WEBFighterNoData.distinct('fighterName')
allwebnames = db.WEBFighterData.distinct('fighterName')

webnodatadisplay.drop() 
#Loops through all fighter info entries
for x in allinfonames:
    #Loops through the web fighter date entries
    isFound = False
    
    for y in allwebnames:
        if x == y:
            #Deletes the info entry if it already exists in the data fighter web entry
            isFound = True
        else:
            print('skip')
            
    if isFound == False:
       document = webfighterinfo.find_one({'fighterName': x})
       webnodatadisplay.insert_one(document)    
 


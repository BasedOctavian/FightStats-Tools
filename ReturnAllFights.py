#Figures out the average stats per each weight class 
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

counter = 0

#Setting Up The Connections To The DB
myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@cluster0.hufkz1t.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]
fighterdata = db["FighterData"]
fights = db["Fights"]

#Get The Fighter Code
#print("Enter First Name")
firstname = input("Enter First Name: ")
firstname = firstname.capitalize()
lastname = input("Enter Last Name: ")
lastname = lastname.capitalize()
nickname = input("Enter Nickname: ")
nickname = nickname.title()
fightercode = firstname + lastname + nickname


print("//////////////////////////////////")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("//////////////////////////////////")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("//////////////////////////////////")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")



adoc = db.Fights.find({"fighterA":fightercode},{"eventCode":1, "fighterA":1, "fighterB":1, "scheduledRounds":1, "actualRounds":1, "finalRoundTime":1, "methodOfFinish":1, "weightClass":1, "isTitleFight":1, "fighterA":1, "_id":0});

bdoc = db.Fights.find({"fighterB":fightercode},{"eventCode":1, "fighterA":1, "fighterB":1, "scheduledRounds":1, "actualRounds":1, "finalRoundTime":1, "methodOfFinish":1, "weightClass":1, "isTitleFight":1, "fighterA":1, "_id":0});


for x in adoc:
    
    print(x)
    print("//////////////////////////////////")
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
    print("")
    print("")
    counter = counter + 1
    
    
for x in bdoc:
    
    print(x)
    print("//////////////////////////////////")
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
    print("")
    print("")
    counter = counter + 1
    
    

    
print("//////////////////////////////////")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("//////////////////////////////////")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("//////////////////////////////////")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("//////////////////////////////////")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")


print(counter, " Fights Tracked")

input("Enter Any Key To Quit")
SystemExit


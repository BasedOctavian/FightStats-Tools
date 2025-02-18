#Figures out the fighters stats in relation to the average stats per each weight class 
import pymongo
myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@octc1.d2he2mx.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]
fighterdata = db["FighterData"]
fighternames = db["FighterNames"]
fights = db["Fights"]
#Get The Weight Class #
weightnum = int()
weightnum = input("Enter Weight Class #: ")
weightnum = int(weightnum)
print("//////////////////////////////////")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("//////////////////////////////////")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("//////////////////////////////////")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")








import pymongo
import collections as ct 

import csv
import sqlite3



#Setting Up The Connections To The DB
myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@octc1.d2he2mx.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]
combos = db["Combinations"]


webfighterdata = db["WEBFighterData"]

allfightercodes = db.WEBFighterData.distinct('fighterCode')


for y in allfightercodes:
    
    
    
    l = db.FighterData.find({"fighterCode":y},{"TotalComboMinutes":1,  "_id":0}).distinct('TotalComboMinutes');
    combomins = l[0]
    
    l = db.Combinations
    fightsTracked = l[0]

    x = l.find({"fighterCode":y},{"_id":0})

    docstring = str()
    split1 = list()
    absorbed = list()

    landed = list()


    if combomins > 5:    
        for document in x:
            #print(document)
            docstring = str(document)
            docstring = docstring.replace(',', '')
            docstring = docstring.replace(':', '')
            docstring = docstring.replace('}', '')
            split1 = docstring.split(",")
            split2 = docstring.split("'")

            
            try:              
                split2.remove(y)
            except ValueError:
                print("not in list")
                db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"1TopCombo": "No Data"}})
                db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"2TopCombo": "No Data"}})
                db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"3TopCombo": "No Data"}})
                continue
            split2.remove("fighterCode")
            split2.remove("{")
            
            while (' ' in split2):
                split2.remove(' ')
            
            for x in split2:
                x.replace(" ", "")
                x.replace("ABS", "")

            

            
            dd = ct.defaultdict(int)
            iterable = iter(split2)
            for word in iterable:
                dd[word] += int(next(iterable)) 
            
            for k in list(dd.keys()):
                if k.startswith('ABS'):
                    del dd[k]
                    
            for k in list(dd.keys()):
                if k.startswith('_'):
                    dacount = k.count("_")
                    if dacount < 3:
                        del dd[k]
            
            
            
            sortedDD = sorted(dd, key=dd.get, reverse=True)[:3]
            
            for o in sortedDD:
                count = o.count('_')
                if count == 1:
                    sortedDD.remove(o)
            new_list = []
            
            total3plus = 0
            
            for entry in sortedDD:
                undercount = entry.lower().count("_")
                
                new_entry = entry.replace("_", " + ")
                new_entry = new_entry[3:]
                split_string = new_entry.split("+")
                if split_string[0].replace(" ", "") != split_string[1].replace(" ", ""):
                    new_list.append(new_entry)

                        
                
                
            
            
            try:     
                db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"1TopCombo": new_list[0]}})
            except:
                db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"1TopCombo": "No Data"}})
            
            try:
                db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"2TopCombo": new_list[1]}})
            except:
                db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"2TopCombo": "No Data"}})
                
            try:
                db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"3TopCombo": new_list[2]}})
            except:
                db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"3TopCombo": "No Data"}})
                
    else:
        db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"1TopCombo": "No Data"}})
        db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"2TopCombo": "No Data"}})
        db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"3TopCombo": "No Data"}})
                
    cagepositions = dict()

    l = db.FighterData.find({"fighterCode":y},{"CenterOctagon":1,  "_id":0}).distinct('CenterOctagon')
    cagepositions.update({"CenterOctagon": l[0]})

    l = db.FighterData.find({"fighterCode":y},{"PushedBackToCage":1,  "_id":0}).distinct('PushedBackToCage')
    cagepositions.update({"PushedBackToCage": l[0]})

    l = db.FighterData.find({"fighterCode":y},{"PushingAgainstCage":1,  "_id":0}).distinct('PushingAgainstCage')
    cagepositions.update({"PushingAgainstCage": l[0]})

    l = db.FighterData.find({"fighterCode":y},{"OnTopGround":1,  "_id":0}).distinct('OnTopGround')
    cagepositions.update({"OnTopGround": l[0]})

    l = db.FighterData.find({"fighterCode":y},{"OnBottomGround":1,  "_id":0}).distinct('OnBottomGround')
    cagepositions.update({"OnBottomGround": l[0]})

    l = db.FighterData.find({"fighterCode":y},{"InClinch":1,  "_id":0}).distinct('InClinch')
    cagepositions.update({"InClinch": l[0]})

    l = db.FighterData.find({"fighterCode":y},{"BeingClinched":1,  "_id":0}).distinct('BeingClinched')
    cagepositions.update({"BeingClinched": l[0]})

    l = db.FighterData.find({"fighterCode":y},{"TotalPositionPoints":1,  "_id":0}).distinct('TotalPositionPoints')
    TotalPositionPoints = int()
    TotalPositionPoints = l[0]

    sortedPOS = list()


    #sortedPOS = sorted(cagepositions.items(), key=lambda x:x[1])

    sortedPOS = sorted(cagepositions, key=cagepositions.get, reverse=True)[:3]

    if sortedPOS[0] == "CenterOctagon":
       sortedPOS[0] =  "Center Octagon"
       
    if sortedPOS[0] == "InClinch":
       sortedPOS[0] = "Initiating Clinch"
       
    if sortedPOS[0] == "BeingClinched":
       sortedPOS[0] = "Being Clinched"
       
    if sortedPOS[0] == "PushingAgainstCage":
       sortedPOS[0] = "Pressuring"
       
    if sortedPOS[0] == "PushedBackToCage":
       sortedPOS[0] = "Moving Backwards"
       
    if sortedPOS[0] == "OnTopGround":
       sortedPOS[0] = "Ground-Top"
       
    if sortedPOS[0] == "OnBottomGround":
       sortedPOS[0] = "Ground-Bottom"
    

    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"1CagePosition": sortedPOS[0]}})
    




input("Done!")
    
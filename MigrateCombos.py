import pymongo
myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@octc1.d2he2mx.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]
fighternames = db["FighterNames"]


mycol = db["FighterData"]

#cursors = db.FighterNames.find({"name": {$regex: REGEX}})


codedoc = db.FighterNames.distinct('fighterCode');


for x in codedoc:
    db.FighterData.update_one({"fighterCode": x}, {"$set": {"TotalComboMinutes": 0}})

print("done")
    
    

    


import pymongo
import csv
import sqlite3


myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@octc1.d2he2mx.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]
fighterdata = db["FighterData"]
fightername = db["FighterNames"]
wcav = db["WCAV"]
webfighterdata = db["WEBFighterData"]

allfightercodes = db.WEBFighterData.distinct('fighterCode')

for x in allfightercodes:
    fightercode = x
    l = db.FighterNames.find({"fighterCode":fightercode},{"weight":1,  "_id":0}).distinct('weight'); weight = l[0]


    l = db.WCAV.find({"weight":weight},{"minutes":1,  "_id":0}).distinct('minutes')
    minutes = l[0]








    

    #Kick Land Rate
    
    l = db.WCAV.find({"weight":weight},{"TotalKicksLanded":1,  "_id":0}).distinct('TotalKicksLanded')
    totalkickslanded = l[0]
    
    l = db.WCAV.find({"weight":weight},{"TotalKicksThrown":1,  "_id":0}).distinct('TotalKicksThrown')
    totalkicksthrown = l[0]
    
    kickrate = (totalkickslanded / totalkicksthrown) * 100
    kickrate = round(kickrate, 1)
    
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"KickLandRateAV": str(kickrate) + "%"}})

    #Punch Land Rate
    
    l = db.WCAV.find({"weight":weight},{"TotalPunchesLanded":1,  "_id":0}).distinct('TotalPunchesLanded')
    totalpuncheslanded = l[0]
    
    l = db.WCAV.find({"weight":weight},{"TotalPunchesThrown":1,  "_id":0}).distinct('TotalPunchesThrown')
    totalpunchesthrown = l[0]
    
    punchrate = (totalpuncheslanded / totalpunchesthrown) * 100
    punchrate = round(punchrate, 1)
    
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"PunchLandRateAV": str(punchrate) + "%"}})
    
    
    
    #Strike Land Rate
    
    l = db.WCAV.find({"weight":weight},{"TotalClinchStrikesMade":1,  "_id":0}).distinct('TotalClinchStrikesMade')
    totalclinchlanded = l[0]
    
    l = db.WCAV.find({"weight":weight},{"TotalClinchStrikesThrown":1,  "_id":0}).distinct('TotalClinchStrikesThrown')
    totalclinchthrown = l[0]
    
    l = db.WCAV.find({"weight":weight},{"TotalGroundStrikesMade":1,  "_id":0}).distinct('TotalGroundStrikesMade')
    totalgroundlanded = l[0]
    
    l = db.WCAV.find({"weight":weight},{"TotalGroundStrikesThrown":1,  "_id":0}).distinct('TotalGroundStrikesThrown')
    totalgroundthrown = l[0]
    
    strikerate = ((totalpuncheslanded + totalkickslanded + totalgroundlanded + totalclinchlanded) / (totalpunchesthrown + totalkicksthrown + totalgroundthrown + totalclinchthrown)) * 100
    
    strikerate = round(strikerate, 1)
    
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"StrikeLandRateAV": str(strikerate) + "%"}})
    
    

    #Knockdowns Per 25
    
    l = db.WCAV.find({"weight":weight},{"numberofknockdowns":1,  "_id":0}).distinct('numberofknockdowns')
    numofknockdowns = (l[0] / minutes) * 25
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"KnockdownsPer25AV": round(numofknockdowns, 1)}})

    #Stuns Per 25
    
    l = db.WCAV.find({"weight":weight},{"numberofstuns":1,  "_id":0}).distinct('numberofstuns')
    numofstuns = (l[0] / minutes) * 25
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"StunsPer25AV": round(numofstuns, 1)}})

    #Times Stunned Per 25
    
    l = db.WCAV.find({"weight":weight},{"timesstunned":1,  "_id":0}).distinct('timesstunned')
    timesstunned = (l[0] / minutes) * 25
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"TimesStunnedPer25AV": round(timesstunned, 1)}})

    #Times Knocked Down Per 25

    l = db.WCAV.find({"weight":weight},{"timesknockeddown":1,  "_id":0}).distinct('timesknockeddown')
    timesknockeddown = (l[0] / minutes) * 25
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"TimesKnockedDownPer25AV": round(timesknockeddown, 1)}})
    
    
    #Sub Attempts Per 25

    l = db.WCAV.find({"weight":weight},{"subattempt":1,  "_id":0}).distinct('subattempt')
    subAttempts = (l[0] / minutes) * 25
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"SubAttemptsPer25AV": round(subAttempts, 1)}})
    
print("Done!")
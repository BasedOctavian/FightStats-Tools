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


allfighterset = set()

#Filter Arguments For Each Weight Class
allfightercodes = db.WEBFighterData.distinct('fighterCode')


for x in allfightercodes:
    y = db.FighterData.find({"fighterCode":x}, {"RoundsTracked":1, "_id":0}).distinct('RoundsTracked')
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"RoundsTracked": y[0]}})
    roundsTracked = y[0]
    y = db.FighterData.find({"fighterCode":x}, {"MinutesTracked":1, "_id":0}).distinct('MinutesTracked')
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"MinutesTracked": y[0]}})
    minutesTracked = y[0]
    
    #Get Takedown Rate
    
    y = db.FighterData.find({"fighterCode":x}, {"SingleLegTakedownSuccess":1, "_id":0}).distinct('SingleLegTakedownSuccess')
    fsinglelegsuccess2 = y[0]
    
    y = db.WEBFighterData.find({"fighterCode":x}, {"height":1, "_id":0}).distinct('height')
    height = y[0]
    
    height2 = str(height)
    
    if "'" in height2:
        print("skip")
    else:
        heightinches = int(height)
        feet = heightinches // 12
        inches = heightinches % 12
        db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"height": f"{feet}'{inches}\"" }})
    
    
    
    y = db.FighterData.find({"fighterCode":x}, {"SingleLegTakedownAttempts":1, "_id":0}).distinct('SingleLegTakedownAttempts')
    fsinglelegattempt2 = y[0]
    y = db.FighterData.find({"fighterCode":x}, {"DoubleLegTakedownSuccess":1, "_id":0}).distinct('DoubleLegTakedownSuccess')
    fdoublelegsuccess2 = y[0]
    y = db.FighterData.find({"fighterCode":x}, {"DoubleLegTakedownAttempts":1, "_id":0}).distinct('DoubleLegTakedownAttempts')
    fdoublelegattempt2 = y[0]
    
    y = db.FighterData.find({"fighterCode":x}, {"TripTakedownSuccess":1, "_id":0}).distinct('DoubleLegTakedownSuccess')
    ftripsuccess2 = y[0]
    y = db.FighterData.find({"fighterCode":x}, {"TripTakedownAttempts":1, "_id":0}).distinct('DoubleLegTakedownAttempts')
    ftripattempt2 = y[0]
    
    y = db.FighterData.find({"fighterCode":x}, {"BodyLockTakedownSuccess":1, "_id":0}).distinct('BodyLockTakedownSuccess')
    fbodylocksuccess2 = y[0]
    y = db.FighterData.find({"fighterCode":x}, {"BodyLockTakedownAttempts":1, "_id":0}).distinct('BodyLockTakedownAttempts')
    fbodylockattempt2 = y[0]
    
    y = db.FighterData.find({"fighterCode":x}, {"SuccessfulThrowTD":1, "_id":0}).distinct('SuccessfulThrowTD')
    fthrowsuccess2 = y[0]
    y = db.FighterData.find({"fighterCode":x}, {"AttemptedThrowTD":1, "_id":0}).distinct('AttemptedThrowTD')
    fthrowattempt2 = y[0]
    
    
    
    if (fsinglelegattempt2 + fdoublelegattempt2 + ftripattempt2 + fthrowattempt2 + fbodylockattempt2) == 0:
        takedownRate = 0
    else :
        takedownRate = ((fsinglelegsuccess2 + fdoublelegsuccess2 + ftripsuccess2 + fthrowsuccess2 + fbodylocksuccess2) / (fsinglelegattempt2 + fdoublelegattempt2 + ftripattempt2 + fthrowattempt2 + fbodylockattempt2)) * 100
        round(takedownRate, 1)
    
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"TakedownRate": (str(round(takedownRate, 1)) + "%" )}})
    singlelegsper25 = (fsinglelegsuccess2 / minutesTracked) * 25
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"SingleLegsPer25": round(singlelegsper25, 1)}})
    
    doublelegsper25 = (fdoublelegsuccess2 / minutesTracked) * 25
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"DoubleLegsPer25": round(doublelegsper25, 1)}})
    
    tripsper25 = (ftripsuccess2 / minutesTracked) * 25
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"TripsPer25": round(tripsper25, 1)}})
    
    bodylocksper25 = (fbodylocksuccess2 / minutesTracked) * 25
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"BodyLocksPer25": round(bodylocksper25, 1)}})
    
    throwsper25 = (fthrowsuccess2 / minutesTracked) * 25
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"ThrowsPer25": round(throwsper25, 1)}})
    
    
    #Get The Times Taken Down Per 25
    
    y = db.FighterData.find({"fighterCode":x}, {"TimesSingleLegged":1, "_id":0}).distinct('TimesSingleLegged')
    timessinglelegged = (y[0] / minutesTracked) * 25
    
    y = db.FighterData.find({"fighterCode":x}, {"TimesDoubleLegged":1, "_id":0}).distinct('TimesDoubleLegged')
    timesdoublelegged = (y[0] / minutesTracked) * 25
    
    y = db.FighterData.find({"fighterCode":x}, {"TimesTripped":1, "_id":0}).distinct('TimesTripped')
    timestripped = (y[0] / minutesTracked) * 25
    
    y = db.FighterData.find({"fighterCode":x}, {"TimesBodyLocked":1, "_id":0}).distinct('TimesBodyLocked')
    timesbodylocked = (y[0] / minutesTracked) * 25
    
    y = db.FighterData.find({"fighterCode":x}, {"TimesThrown":1, "_id":0}).distinct('TimesThrown')
    timesthrown = (y[0] / minutesTracked) * 25
    
    
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"TimesSingleLegsPer25": round(timessinglelegged, 1)}})
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"TimesDoubleLegsPer25": round(timesdoublelegged, 1)}})
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"TimesTripsPer25": round(timestripped, 1)}})
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"TimesBodyLocksPer25": round(timesbodylocked, 1)}})
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"TimesThrowsPer25": round(timesthrown, 1)}})
    
    
    
    #Strike Land Rate
    
    
    
    y = db.FighterData.find({"fighterCode":x}, {"TotalClinchStrikesMade":1, "_id":0}).distinct('TotalClinchStrikesMade')
    ftotalclinchstrikeslanded = y[0] 
    y = db.FighterData.find({"fighterCode":x}, {"TotalClinchStrikesThrown":1, "_id":0}).distinct('TotalClinchStrikesThrown')
    ftotalclinchstrikesthrown = y[0] 
    
    y = db.FighterData.find({"fighterCode":x}, {"TotalGroundStrikesMade":1, "_id":0}).distinct('TotalGroundStrikesMade')
    ftotalgroundstrikeslanded = y[0] 
    y = db.FighterData.find({"fighterCode":x}, {"TotalGroundStrikesThrown":1, "_id":0}).distinct('TotalGroundStrikesThrown')
    ftotalgroundstrikesthrown = y[0] 
    
    y = db.FighterData.find({"fighterCode":x}, {"TotalKicksLanded":1, "_id":0}).distinct('TotalKicksLanded')
    ftotalkickslanded = y[0] 
    y = db.FighterData.find({"fighterCode":x}, {"TotalKicksThrown":1, "_id":0}).distinct('TotalKicksThrown')
    ftotalkicksthrown = y[0] 
    
    y = db.FighterData.find({"fighterCode":x}, {"TotalPunchesLanded":1, "_id":0}).distinct('TotalPunchesLanded')
    ftotalpuncheslanded = y[0] 
    y = db.FighterData.find({"fighterCode":x}, {"TotalPunchesThrown":1, "_id":0}).distinct('TotalPunchesThrown')
    ftotalpunchesthrown = y[0] 
    
    
    strikeLandRate = ((ftotalclinchstrikeslanded + ftotalgroundstrikeslanded + ftotalkickslanded + ftotalpuncheslanded) / (ftotalclinchstrikesthrown + ftotalgroundstrikesthrown + ftotalkicksthrown + ftotalpunchesthrown)) * 100
    
    strikeLandRate = round(strikeLandRate, 1)
    
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"StrikeLandRate": (str(strikeLandRate) + "%")}})
    
    
    kickslmp = float()
    
    #Kicks Landed Per Minute
    kickslmp = (ftotalkickslanded / minutesTracked)
    kickslmp = round(kickslmp, 1)
    
    
    kickstmp = float()
    
    #Kicks Thrown Per Minute
    kickstmp = (ftotalkicksthrown / minutesTracked)
    kickstmp = round(kickstmp, 1)
    
    puncheslmp = float()
    
    #Punches Landed Per Minute
    puncheslmp = (ftotalpuncheslanded / minutesTracked)
    puncheslmp = round(puncheslmp, 1)
    
    strikestmp = float()
    
    #Punches Thrown Per Minute
    punchestmp = (ftotalpunchesthrown / minutesTracked)
    punchestmp = round(punchestmp, 1)
    
    strikeslmp = float()
    
    #Strikes Landed Per Minute
    strikeslmp = ((ftotalclinchstrikeslanded + ftotalgroundstrikeslanded + ftotalkickslanded + ftotalpuncheslanded) / minutesTracked)
    strikeslmp = round(strikeslmp, 1)
    
    strikestmp = float()
    
    strikestmp = ((ftotalclinchstrikesthrown + ftotalgroundstrikesthrown + ftotalkicksthrown + ftotalpunchesthrown) / minutesTracked)
    strikestmp = round(strikestmp, 1)
    
   
    
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"StrikesLPM": strikeslmp}})
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"StrikesTPM": strikestmp}})
    
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"KicksLPM": kickslmp}})
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"KicksTPM": kickstmp}})
    
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"PunchesLPM": puncheslmp}})
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"PunchesTPM": punchestmp}})
    
    
    if ftotalkickslanded < 1:
        kickLandRate = 0
        
    else:
        kickLandRate = (ftotalkickslanded / ftotalkicksthrown) * 100
        kickLandRate = round(kickLandRate, 1)
    
    
    
    if ftotalpuncheslanded < 1:
        punchLandRate = 0
        
    else: 
        punchLandRate = (ftotalpuncheslanded / ftotalpunchesthrown) * 100
        punchLandRate = round(punchLandRate, 1)
    
    
    
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"KickLandRate": (str(kickLandRate) + "%")}})
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"PunchLandRate": (str(punchLandRate) + "%")}})
    
    
    #Knockdowns & Stuns
    
    y = db.FighterData.find({"fighterCode":x}, {"NumberOfKnockDowns":1, "_id":0}).distinct('NumberOfKnockDowns')
    knockdownsper25 = (y[0] / minutesTracked) * 25
    y = db.FighterData.find({"fighterCode":x}, {"NumberOfStuns":1, "_id":0}).distinct('NumberOfStuns')
    stunsper25 = (y[0] / minutesTracked) * 25
    
    y = db.FighterData.find({"fighterCode":x}, {"TimesKnockedDown":1, "_id":0}).distinct('TimesKnockedDown')
    timesknockeddownper25 = (y[0] / minutesTracked) * 25
    y = db.FighterData.find({"fighterCode":x}, {"TimesStunned":1, "_id":0}).distinct('TimesStunned')
    timesstunnedper25 = (y[0] / minutesTracked) * 25
    
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"TimesStunnedPer25": round(timesstunnedper25, 1)}})
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"TimesKnockedDownPer25": round(timesknockeddownper25, 1)}})
    
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"KnockdownsPer25": round(knockdownsper25, 1)}})
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"StunsPer25": round(stunsper25, 1)}})
    
    
    #Get Sub Attempts
    
    y = db.FighterData.find({"fighterCode":x}, {"SubAttempts":1, "_id":0}).distinct('SubAttempts')
    subattemptsper25 = (y[0] / minutesTracked) * 25
    
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"SubAttemptsPer25": round(subattemptsper25, 1)}})
    
    #Stance Data
    
    y = db.FighterData.find({"fighterCode":x}, {"SwitchWins":1, "_id":0}).distinct('SwitchWins')
    switchfights = y[0]
    y = db.FighterData.find({"fighterCode":x}, {"SwitchLosses":1, "_id":0}).distinct('SwitchLosses')
    switchfights = y[0] + switchfights
    
    y = db.FighterData.find({"fighterCode":x}, {"SouthpawWins":1, "_id":0}).distinct('SouthpawWins')
    southpawfights = y[0]
    y = db.FighterData.find({"fighterCode":x}, {"SouthpawLosses":1, "_id":0}).distinct('SouthpawLosses')
    southpawfights = y[0] + southpawfights
    
    y = db.FighterData.find({"fighterCode":x}, {"OrthodoxWins":1, "_id":0}).distinct('OrthodoxWins')
    orthodoxfights = y[0]
    y = db.FighterData.find({"fighterCode":x}, {"OrthodoxLosses":1, "_id":0}).distinct('OrthodoxLosses')
    orthodoxfights = y[0] + orthodoxfights
    
    if orthodoxfights == southpawfights or switchfights == orthodoxfights:
        db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"1Stance": "Switch"}})
        
    if orthodoxfights > southpawfights and orthodoxfights > switchfights:
        db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"1Stance": "Orthodox"}})
        
    if southpawfights > orthodoxfights and southpawfights > switchfights:
        db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"1Stance": "Southpaw"}})
        
    if switchfights > orthodoxfights and switchfights > southpawfights:
        db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"1Stance": "Switch"}})
        
        
    y = db.FighterData.find({"fighterCode":x}, {"WinsVsSwitch":1, "_id":0}).distinct('WinsVsSwitch')
    winsvsswitch = y[0]
    
    y = db.FighterData.find({"fighterCode":x}, {"LossesVsSwitch":1, "_id":0}).distinct('LossesVsSwitch')
    lossesvsswitch = y[0]
    
    switchrecord = str(winsvsswitch) + "-" + str(lossesvsswitch)
    
    y = db.FighterData.find({"fighterCode":x}, {"WinsVsOrthodox":1, "_id":0}).distinct('WinsVsOrthodox')
    winsvsorthodox = y[0]
    
    y = db.FighterData.find({"fighterCode":x}, {"LossesVsOrthodox":1, "_id":0}).distinct('LossesVsOrthodox')
    lossesvsorthodox = y[0]
    
    orthodoxrecord = str(winsvsorthodox) + "-" + str(lossesvsorthodox)
    
    y = db.FighterData.find({"fighterCode":x}, {"WinsVsSouthpaw":1, "_id":0}).distinct('WinsVsSouthpaw')
    winsvssouthpaw = y[0]
    
    y = db.FighterData.find({"fighterCode":x}, {"LossesVsSouthpaw":1, "_id":0}).distinct('LossesVsSouthpaw')
    lossesvssouthpaw = y[0]
    
    southpawrecord = str(winsvssouthpaw) + "-" + str(lossesvssouthpaw)
    
    
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"RecordAgainstSwitch": str(switchrecord)}})
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"RecordAgainstOrthodox": str(orthodoxrecord)}})
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"RecordAgainstSouthpaw": str(southpawrecord)}})
    
    #Get Position Percents
    standingstrikes = ftotalpuncheslanded + ftotalkickslanded
    clinchstrikes = ftotalclinchstrikeslanded
    groundstrikes = ftotalgroundstrikeslanded
    total = standingstrikes + clinchstrikes + groundstrikes
    
    
    
    standingpercent = (standingstrikes/total) * 100
    standingpercent = int(round(standingpercent))
    clinchpercent = (clinchstrikes/total) * 100
    clinchpercent = int(round(clinchpercent))
    groundpercent = (groundstrikes/total) * 100
    groundpercent = int(round(groundpercent))
    
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"standingPOSStrikes": str(standingpercent) + '%'}})
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"clinchPOSStrikes": str(clinchpercent) + '%'}})
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"groundPOSStrikes": str(groundpercent) + '%'}})
    
    y = db.FighterData.find({"fighterCode":x}, {"SingleLegDefends":1, "_id":0}).distinct('SingleLegDefends')
    singlelegdefends = y[0]
    y = db.FighterData.find({"fighterCode":x}, {"DoubleLegDefends":1, "_id":0}).distinct('DoubleLegDefends')
    doublelegdefends = y[0]
    y = db.FighterData.find({"fighterCode":x}, {"TripDefends":1, "_id":0}).distinct('TripDefends')
    tripdefends = y[0]
    y = db.FighterData.find({"fighterCode":x}, {"BodyLockDefends":1, "_id":0}).distinct('BodyLockDefends')
    bodylockdefends = y[0]
    y = db.FighterData.find({"fighterCode":x}, {"ThrowDefends":1, "_id":0}).distinct('ThrowDefends')
    throwdefends = y[0]
    
    
    timestakendown = timessinglelegged + timesdoublelegged + timesbodylocked + timestripped + timesthrown
    timesdefended = singlelegdefends + doublelegdefends + bodylockdefends + tripdefends + throwdefends
    totalattemptsagainst = timestakendown + timesdefended
    try:
        tddefensepercent = (timesdefended/totalattemptsagainst) * 100
    except:
        tddefensepercent = 0
    tddefensepercent = int(round(tddefensepercent))
    db.WEBFighterData.update_one({"fighterCode":x}, {"$set": {"TDDefense": str(tddefensepercent) + '%'}})
    
    
    
    
print("Done!")  
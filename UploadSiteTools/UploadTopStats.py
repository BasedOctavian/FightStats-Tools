import pymongo
import csv
import sqlite3


fightsTracked = int()
minutesTracked = int()



topStrikesAbsorbed = list()
topTakedownsLanded = list()
topTakedownsAbsorbed = list()
topStrikesThrown = list()


#Setting Up The Connections To The DB
myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@octc1.d2he2mx.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]
fighterdata = db["FighterData"]
webfighterdata = db["WEBFighterData"]

allfightercodes = db.WEBFighterData.distinct('fighterCode')


for y in allfightercodes:
    l = db.FighterData.find({"fighterCode":y},{"FightsTracked":1,  "_id":0}).distinct('FightsTracked')
    fightsTracked = l[0]
    l = db.FighterData.find({"fighterCode":y},{"MinutesTracked":1,  "_id":0}).distinct('MinutesTracked');
    minutesTracked = l[0]

    total20strikesmade = 0
    
    l = db.FighterData.find({"fighterCode":y},{"GroundStrikeHiMake":1,  "_id":0}).distinct('GroundStrikeHiMake');
    groundstrikeshead = l[0]
    total20strikesmade = total20strikesmade + l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"GroundStrikeLoMake":1,  "_id":0}).distinct('GroundStrikeLoMake');
    groundstrikesbody = l[0]
    total20strikesmade = total20strikesmade + l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"ClinchStrikeHiMake":1,  "_id":0}).distinct('ClinchStrikeHiMake');
    clinchstrikeshead = l[0]
    total20strikesmade = total20strikesmade + l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"ClinchStrikeLoMake":1,  "_id":0}).distinct('ClinchStrikeLoMake');
    clinchstrikesbody = l[0]
    total20strikesmade = total20strikesmade + l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"TotalElbowsMade":1,  "_id":0}).distinct('TotalElbowsMade');
    totalelbowsmade = l[0]
    total20strikesmade = total20strikesmade + l[0]


    l = db.FighterData.find({"fighterCode":y},{"LeftJabHiMake":1,  "_id":0}).distinct('LeftJabHiMake');
    leftHiJab = l[0]
    l = db.FighterData.find({"fighterCode":y},{"LeftJabLoMake":1,  "_id":0}).distinct('LeftJabLoMake');
    leftLoJab = l[0]

    l = db.FighterData.find({"fighterCode":y},{"RightJabHiMake":1,  "_id":0}).distinct('RightJabHiMake');
    RightHiJab = l[0]
    l = db.FighterData.find({"fighterCode":y},{"RightJabLoMake":1,  "_id":0}).distinct('RightJabLoMake');
    RightLoJab = l[0]


    l = db.FighterData.find({"fighterCode":y},{"LeftStraightHiMake":1,  "_id":0}).distinct('LeftStraightHiMake');
    leftHiStraight = l[0]
    l = db.FighterData.find({"fighterCode":y},{"LeftStraightLoMake":1,  "_id":0}).distinct('LeftStraightLoMake');
    leftLoStraight = l[0]

    l = db.FighterData.find({"fighterCode":y},{"RightStraightHiMake":1,  "_id":0}).distinct('RightStraightHiMake');
    RightHiStraight = l[0]
    l = db.FighterData.find({"fighterCode":y},{"RightStraightLoMake":1,  "_id":0}).distinct('RightStraightLoMake');
    RightLoStraight = l[0]


    l = db.FighterData.find({"fighterCode":y},{"LeftHookHiMake":1,  "_id":0}).distinct('LeftHookHiMake');
    leftHiHook = l[0]
    l = db.FighterData.find({"fighterCode":y},{"LeftHookLoMake":1,  "_id":0}).distinct('LeftHookLoMake');
    leftLoHook = l[0]

    l = db.FighterData.find({"fighterCode":y},{"RightHookHiMake":1,  "_id":0}).distinct('RightHookHiMake');
    RightHiHook = l[0]
    l = db.FighterData.find({"fighterCode":y},{"RightHookLoMake":1,  "_id":0}).distinct('RightHookLoMake');
    RightLoHook = l[0]


    l = db.FighterData.find({"fighterCode":y},{"LeftUppercutHiMake":1,  "_id":0}).distinct('LeftUppercutHiMake');
    leftHiUppercut = l[0]
    l = db.FighterData.find({"fighterCode":y},{"LeftUppercutLoMake":1,  "_id":0}).distinct('LeftUppercutLoMake');
    leftLoUppercut = l[0]

    l = db.FighterData.find({"fighterCode":y},{"RightUppercutHiMake":1,  "_id":0}).distinct('RightUppercutHiMake');
    RightHiUppercut = l[0]
    l = db.FighterData.find({"fighterCode":y},{"RightUppercutLoMake":1,  "_id":0}).distinct('RightUppercutLoMake');
    RightLoUppercut = l[0]


    l = db.FighterData.find({"fighterCode":y},{"LeftLegKickMake":1,  "_id":0}).distinct('LeftLegKickMake');
    leftLegKick = l[0]
    l = db.FighterData.find({"fighterCode":y},{"LeftLegKickMake":1,  "_id":0}).distinct('LeftLegKickMake');
    leftLegKick = l[0]

    l = db.FighterData.find({"fighterCode":y},{"RightLegKickMake":1,  "_id":0}).distinct('RightLegKickMake');
    RightLegKick = l[0]
    l = db.FighterData.find({"fighterCode":y},{"RightLegKickMake":1,  "_id":0}).distinct('RightLegKickMake');
    RightLegKick = l[0]




    l = db.FighterData.find({"fighterCode":y},{"LeftBodyKickMake":1,  "_id":0}).distinct('LeftBodyKickMake');
    leftBodyKick = l[0]
    l = db.FighterData.find({"fighterCode":y},{"LeftBodyKickMake":1,  "_id":0}).distinct('LeftBodyKickMake');
    leftBodyKick = l[0]

    l = db.FighterData.find({"fighterCode":y},{"RightBodyKickMake":1,  "_id":0}).distinct('RightBodyKickMake');
    RightBodyKick = l[0]
    l = db.FighterData.find({"fighterCode":y},{"RightBodyKickMake":1,  "_id":0}).distinct('RightBodyKickMake');
    RightBodyKick = l[0]



    l = db.FighterData.find({"fighterCode":y},{"LeftHighKickMake":1,  "_id":0}).distinct('LeftHighKickMake');
    leftHighKick = l[0]
    l = db.FighterData.find({"fighterCode":y},{"LeftHighKickMake":1,  "_id":0}).distinct('LeftHighKickMake');
    leftHighKick = l[0]

    l = db.FighterData.find({"fighterCode":y},{"RightHighKickMake":1,  "_id":0}).distinct('RightHighKickMake');
    RightHighKick = l[0]
    l = db.FighterData.find({"fighterCode":y},{"RightHighKickMake":1,  "_id":0}).distinct('RightHighKickMake');
    RightHighKick = l[0]

    l = db.FighterData.find({"fighterCode":y},{"RightOverhandMake":1,  "_id":0}).distinct('RightOverhandMake');
    rightOverhandMake = l[0]
    l = db.FighterData.find({"fighterCode":y},{"LeftOverhandMake":1,  "_id":0}).distinct('LeftOverhandMake');
    leftOverhandMake = l[0]



    l = db.FighterData.find({"fighterCode":y},{"SingleLegTakedownAttempts":1,  "_id":0}).distinct('SingleLegTakedownAttempts');
    singleLegTakedownAttempts = l[0]

    l = db.FighterData.find({"fighterCode":y},{"DoubleLegTakedownAttempts":1,  "_id":0}).distinct('DoubleLegTakedownAttempts');
    doubleLegTakedownAttempts = l[0]

    l = db.FighterData.find({"fighterCode":y},{"TripTakedownAttempts":1,  "_id":0}).distinct('TripTakedownAttempts');
    tripTakedownAttempts = l[0]

    l = db.FighterData.find({"fighterCode":y},{"BodyLockTakedownAttempts":1,  "_id":0}).distinct('BodyLockTakedownAttempts');
    bodyLockTakedownAttempts = l[0]

    l = db.FighterData.find({"fighterCode":y},{"AttemptedThrowTD":1,  "_id":0}).distinct('AttemptedThrowTD');
    throwTakedownAttempts = l[0]





    l = db.FighterData.find({"fighterCode":y},{"TimesBodyLocked":1,  "_id":0}).distinct('TimesBodyLocked');
    timesBodyLocked = l[0]

    l = db.FighterData.find({"fighterCode":y},{"TimesTripped":1,  "_id":0}).distinct('TimesTripped');
    timesTripped = l[0]

    l = db.FighterData.find({"fighterCode":y},{"TimesDoubleLegged":1,  "_id":0}).distinct('TimesDoubleLegged');
    timesDoubleLegged = l[0]

    l = db.FighterData.find({"fighterCode":y},{"TimesSingleLegged":1,  "_id":0}).distinct('TimesSingleLegged');
    timesSingleLegged = l[0]

    l = db.FighterData.find({"fighterCode":y},{"TimesThrown":1,  "_id":0}).distinct('TimesThrown');
    TimesThrown = l[0]


    l = db.FighterData.find({"fighterCode":y},{"BodyKicksAbsorbed":1,  "_id":0}).distinct('BodyKicksAbsorbed');
    BodyKicksAbsorbed = l[0]

    l = db.FighterData.find({"fighterCode":y},{"HeadKicksAbsorbed":1,  "_id":0}).distinct('HeadKicksAbsorbed');
    HeadKicksAbsorbed = l[0]

    l = db.FighterData.find({"fighterCode":y},{"LegKicksAbsorbed":1,  "_id":0}).distinct('LegKicksAbsorbed');
    LegKicksAbsorbed = l[0]

    l = db.FighterData.find({"fighterCode":y},{"UppercutsAbsorbed":1,  "_id":0}).distinct('UppercutsAbsorbed');
    UppercutsAbsorbed = l[0]

    l = db.FighterData.find({"fighterCode":y},{"HooksAbsorbed":1,  "_id":0}).distinct('HooksAbsorbed');
    HooksAbsorbed = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"OverhandsAbsorbed":1,  "_id":0}).distinct('OverhandsAbsorbed');
    OverhandsAbsorbed = l[0]

    l = db.FighterData.find({"fighterCode":y},{"StraightsAbsorbed":1,  "_id":0}).distinct('StraightsAbsorbed');
    StraightsAbsorbed = l[0]

    l = db.FighterData.find({"fighterCode":y},{"JabsAbsorbed":1,  "_id":0}).distinct('JabsAbsorbed');
    JabsAbsorbed = l[0]
    
    
    l = db.FighterData.find({"fighterCode":y},{"Round1StrikesLanded":1,  "_id":0}).distinct('Round1StrikesLanded');
    round1strikes = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"Round2StrikesLanded":1,  "_id":0}).distinct('Round2StrikesLanded');
    round2strikes = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"Round3StrikesLanded":1,  "_id":0}).distinct('Round3StrikesLanded');
    round3strikes = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"Round4StrikesLanded":1,  "_id":0}).distinct('Round4StrikesLanded');
    round4strikes = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"Round5StrikesLanded":1,  "_id":0}).distinct('Round5StrikesLanded');
    round5strikes = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"StrikingGameplans":1,  "_id":0}).distinct('StrikingGameplans');
    strikingGameplans = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"GrapplingGameplans":1,  "_id":0}).distinct('GrapplingGameplans');
    grapplingGameplans = l[0]

    
    
    punchapm = (JabsAbsorbed + StraightsAbsorbed + HooksAbsorbed + UppercutsAbsorbed) / minutesTracked
    
    punchapm = float(punchapm)
    
    kicksapm = float()
    
    kicksapm = (BodyKicksAbsorbed + HeadKicksAbsorbed + LegKicksAbsorbed) / minutesTracked
    
    kicksapm = float(kicksapm)
    
    strikesapm = punchapm + kicksapm

    strikesLanded = dict()
    
    
    strikesLanded.update({"Left Jab to Head": (leftHiJab / minutesTracked) * 25})
    strikesLanded.update({"Left Jab to Body": (leftLoJab / minutesTracked) * 25})
    strikesLanded.update({"Right Jab to Head": (RightHiJab / minutesTracked) * 25})
    strikesLanded.update({"Right Jab to Body": (RightLoJab / minutesTracked) * 25})
    strikesLanded.update({"Left Straight to Head": (leftHiStraight / minutesTracked) * 25})
    strikesLanded.update({"Left Straight to Body": (leftLoStraight / minutesTracked) * 25})
    strikesLanded.update({"Right Straight to Head": (RightHiStraight / minutesTracked) * 25})
    strikesLanded.update({"Right Straight to Body": (RightLoStraight / minutesTracked) * 25})
    strikesLanded.update({"Left Hook to Head": (leftHiHook / minutesTracked) * 25})
    strikesLanded.update({"Left Hook to Body": (leftLoHook / minutesTracked) * 25})
    strikesLanded.update({"Right Hook to Head": (RightHiHook / minutesTracked) * 25})
    strikesLanded.update({"Right Hook to Body": (RightLoHook / minutesTracked) * 25})
    strikesLanded.update({"Left Uppercut to Head": (leftHiUppercut / minutesTracked) * 25})
    strikesLanded.update({"Left Uppercut to Body": (leftLoUppercut / minutesTracked) * 25})
    strikesLanded.update({"Right Uppercut to Head": (RightHiUppercut / minutesTracked) * 25})
    strikesLanded.update({"Right Uppercut to Body": (RightLoUppercut / minutesTracked) * 25})
    strikesLanded.update({"Right Overhand": (rightOverhandMake / minutesTracked) * 25})
    strikesLanded.update({"Left Overhand": (leftOverhandMake / minutesTracked) * 25})
    strikesLanded.update({"Right Head Kick": (RightHighKick / minutesTracked) * 25})
    strikesLanded.update({"Left Head Kick": (leftHighKick / minutesTracked) * 25})
    strikesLanded.update({"Right Body Kick": (RightBodyKick / minutesTracked) * 25})
    strikesLanded.update({"Left Body Kick": (leftBodyKick / minutesTracked) * 25})
    strikesLanded.update({"Right Leg Kick": (RightLegKick / minutesTracked) * 25})
    strikesLanded.update({"Left Leg Kick": (leftLegKick / minutesTracked) * 25})


    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"grapplingGameplans": grapplingGameplans}})
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"strikingGameplans": strikingGameplans}})

    #Gets The Round By Round Strike Land Percentage
    totalroundStrikes = round1strikes + round2strikes + round3strikes + round4strikes + round5strikes
    
    tempy = (round1strikes / totalroundStrikes) * 100
    tempy = round(tempy, 1)
    strtempy = str(tempy)
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"Round1StrikesLanded": strtempy + "%"}})
    
    tempy = (round2strikes / totalroundStrikes) * 100
    tempy = round(tempy, 1)
    strtempy = str(tempy)
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"Round2StrikesLanded": strtempy + "%"}})
    
    tempy = (round3strikes / totalroundStrikes) * 100
    tempy = round(tempy, 1)
    strtempy = str(tempy)
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"Round3StrikesLanded": strtempy + "%"}})
    
    tempy = (round4strikes / totalroundStrikes) * 100
    tempy = round(tempy, 1)
    strtempy = str(tempy)
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"Round4StrikesLanded": strtempy + "%"}})
    
    tempy = (round5strikes / totalroundStrikes) * 100
    tempy = round(tempy, 1)
    strtempy = str(tempy)
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"Round5StrikesLanded": strtempy + "%"}})



    tempy = (timesSingleLegged / minutesTracked) * 25
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"TimesSingleLegsPer25": round(tempy, 1)}})
    
    tempy = (timesDoubleLegged / minutesTracked) * 25
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"TimesDoubleLegsPer25": round(tempy, 1)}})
    
    tempy = (timesTripped / minutesTracked) * 25
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"TimesTripsPer25": round(tempy, 1)}})
    
    tempy = (timesBodyLocked / minutesTracked) * 25
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"TimesBodyLocksPer25": round(tempy, 1)}})
    
    tempy = (TimesThrown / minutesTracked) * 25
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"TimesThrowsPer25": round(tempy, 1)}})


    sortedStrikes = sorted(strikesLanded, key=strikesLanded.get, reverse=True)[:3]
    
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"1StrikeLanded": sortedStrikes[0]}})
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"2StrikeLanded": sortedStrikes[1]}})
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"3StrikeLanded": sortedStrikes[2]}})

    
    strikesAbsorbed = dict()
    
    
    strikesAbsorbed.update({"Jabs": (JabsAbsorbed / minutesTracked) * 5})
    strikesAbsorbed.update({"Hooks": (HooksAbsorbed / minutesTracked) * 5})
    strikesAbsorbed.update({"Crosses": (StraightsAbsorbed / minutesTracked) * 5})
    strikesAbsorbed.update({"Uppercuts": (UppercutsAbsorbed / minutesTracked) * 5})
    strikesAbsorbed.update({"Head Kicks": (HeadKicksAbsorbed / minutesTracked) * 5})
    strikesAbsorbed.update({"Body Kicks": (BodyKicksAbsorbed / minutesTracked) * 5})
    strikesAbsorbed.update({"Leg Kicks": (LegKicksAbsorbed / minutesTracked) * 5})
    
    
    sortedAbsStrikes = sorted(strikesAbsorbed, key=strikesAbsorbed.get, reverse=True)[:3]
    
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"1StrikeAbsorbed": sortedAbsStrikes[0]}})
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"2StrikeAbsorbed": sortedAbsStrikes[1]}})
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"3StrikeAbsorbed": sortedAbsStrikes[2]}})
    

    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"punchapm": round(punchapm, 1)}})
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"kickapm": round(kicksapm, 1)}})
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"strikeapm": round(strikesapm, 1)}})
    #Left Jab

    
    
    l = db.FighterData.find({"fighterCode":y},{"LeftJabHiMake":1,  "_id":0}).distinct('LeftJabHiMake')
    total20strikesmade = total20strikesmade + l[0]
    leftjabhimake = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"LeftJabLoMake":1,  "_id":0}).distinct('LeftJabLoMake')
    total20strikesmade = total20strikesmade + l[0]
    leftjablomake = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"RightJabHiMake":1,  "_id":0}).distinct('RightJabHiMake')
    total20strikesmade = total20strikesmade + l[0]
    rightjabhimake = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"RightJabLoMake":1,  "_id":0}).distinct('RightJabLoMake')
    total20strikesmade = total20strikesmade + l[0]
    rightjablomake = l[0]
    
    
    
    l = db.FighterData.find({"fighterCode":y},{"LeftStraightHiMake":1,  "_id":0}).distinct('LeftStraightHiMake')
    total20strikesmade = total20strikesmade + l[0]
    leftstraighthimake = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"LeftStraightLoMake":1,  "_id":0}).distinct('LeftStraightLoMake')
    total20strikesmade = total20strikesmade + l[0]
    leftstraightlomake = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"RightStraightHiMake":1,  "_id":0}).distinct('RightStraightHiMake')
    total20strikesmade = total20strikesmade + l[0]
    rightstraighthimake = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"RightStraightLoMake":1,  "_id":0}).distinct('RightStraightLoMake')
    total20strikesmade = total20strikesmade + l[0]
    rightstraightlomake = l[0]
    
    
    
    l = db.FighterData.find({"fighterCode":y},{"LeftHookHiMake":1,  "_id":0}).distinct('LeftHookHiMake')
    total20strikesmade = total20strikesmade + l[0]
    lefthookhimake = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"LeftHookLoMake":1,  "_id":0}).distinct('LeftHookLoMake')
    total20strikesmade = total20strikesmade + l[0]
    lefthooklomake = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"RightHookHiMake":1,  "_id":0}).distinct('RightHookHiMake')
    total20strikesmade = total20strikesmade + l[0]
    righthookhimake = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"RightHookLoMake":1,  "_id":0}).distinct('RightHookLoMake')
    total20strikesmade = total20strikesmade + l[0]
    righthooklomake = l[0]
    
    
    
    l = db.FighterData.find({"fighterCode":y},{"LeftOverhandMake":1,  "_id":0}).distinct('LeftOverhandMake')
    total20strikesmade = total20strikesmade + l[0]
    leftoverhandmake = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"RightOverhandMake":1,  "_id":0}).distinct('RightOverhandMake')
    total20strikesmade = total20strikesmade + l[0]
    rightoverhandmake = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"LeftLegKickMake":1,  "_id":0}).distinct('LeftLegKickMake')
    total20strikesmade = total20strikesmade + l[0]
    leftlegkickmake = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"RightLegKickMake":1,  "_id":0}).distinct('RightLegKickMake')
    total20strikesmade = total20strikesmade + l[0]
    rightlegkickmake = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"LeftBodyKickMake":1,  "_id":0}).distinct('LeftBodyKickMake')
    total20strikesmade = total20strikesmade + l[0]
    leftbodykickmake = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"RightBodyKickMake":1,  "_id":0}).distinct('RightBodyKickMake')
    total20strikesmade = total20strikesmade + l[0]
    rightbodykickmake = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"LeftHighKickMake":1,  "_id":0}).distinct('LeftHighKickMake')
    total20strikesmade = total20strikesmade + l[0]
    lefthighkickmake = l[0]
    
    l = db.FighterData.find({"fighterCode":y},{"RightHighKickMake":1,  "_id":0}).distinct('RightHighKickMake')
    total20strikesmade = total20strikesmade + l[0]
    righthighkickmake = l[0]
    
    
    temp2 = (lefthighkickmake / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"LeftHiKick": temp}})
    
    temp2 = (righthighkickmake / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"RightHiKick": temp}})
    
    temp2 = (leftbodykickmake / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"LeftBodyKick": temp}})
    
    temp2 = (rightbodykickmake / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"RightBodyKick": temp}})
    
    temp2 = (leftlegkickmake / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"LeftLegKick": temp}})
    
    temp2 = (rightlegkickmake / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"RightLegKick": temp}})
    
    
    
    
    
    
    
    temp2 = (leftjabhimake / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"LeftJabHiMake": temp}})
    
    temp2 = (leftjablomake / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"LeftJabLoMake": temp}})
    
    temp2 = (rightjabhimake / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"RightJabHiMake": temp}})\
    
    
    temp2 = (rightjablomake / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"RightJabLoMake": temp}})
    
    
    temp2 = (leftstraighthimake / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"LeftStraightHiMake": temp}})
    
    temp2 = (leftstraightlomake / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"LeftStraightLoMake": temp}})
    
    temp2 = (rightstraighthimake / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"RightStraightHiMake": temp}})
    
    temp2 = (rightstraightlomake / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"RightStraightLoMake": temp}})
    
    
    
    
    
    
    
    temp2 = (lefthookhimake / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"LeftHookHiMake": temp}})
    
    temp2 = (lefthooklomake / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"LeftHookLoMake": temp}})
    
    
    
    temp2 = (righthookhimake / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"RightHookHiMake": temp}})
    
    temp2 = (righthooklomake / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"RightHookLoMake": temp}})
    
    
    temp2 = (leftoverhandmake / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"LeftOverhandMake": temp}})
    
    temp2 = (rightoverhandmake / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"RightOverhandMake": temp}})
    
    
    
    
    
    temp2 = (groundstrikeshead / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"TotalGroundStrikesToTheHead": temp}})
    
    temp2 = (groundstrikesbody / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"TotalGroundStrikesToTheBody": temp}})
    

    temp2 = (clinchstrikeshead / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"TotalClinchStrikesToTheHead": temp}})
    

    temp2 = (clinchstrikesbody / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"TotalClinchStrikesToTheBody": temp}})
    

    temp2 = (totalelbowsmade / total20strikesmade) * 100
    temp2 = round(temp2, 1)
    temp = str(temp2)
    temp = temp + "%"
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"TotalElbows": temp}})
    
    lefthandmake = leftHiJab + leftLoJab + leftHiHook + leftLoHook + leftHiStraight + leftLoStraight + leftLoUppercut + leftHiUppercut + leftoverhandmake
    
    righthandmake = RightHiJab + RightLoJab + RightHiHook + RightLoHook + RightHiStraight + RightLoStraight + RightLoUppercut + RightHiUppercut + rightoverhandmake
    
    bothhands = lefthandmake + righthandmake
    
    try:
        lefthandpercent = (lefthandmake/bothhands) * 100
    except:
        lefthandpercent = 0
        
        
    lefthandpercent = int(round(lefthandpercent))
    
    try:
        righthandpercent = (righthandmake/bothhands) * 100
    except:
        righthandpercent = 0    
    
    righthandpercent = int(round(righthandpercent))
    
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"LeftHandThrowPercent": str(lefthandpercent) + '%'}})
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"RightHandThrowPercent": str(righthandpercent) + '%'}})
    
    #Get Head Body Leg Targeting
    
    headtargeting = leftHiJab + RightHiJab + leftHiHook + RightHiHook + leftHiStraight + RightHiStraight + leftHiUppercut + RightHiUppercut + leftoverhandmake + rightoverhandmake + totalelbowsmade + clinchstrikeshead + leftHighKick + RightHighKick
    
    bodytargeting = leftLoJab + RightLoJab + leftLoHook + RightLoHook + leftLoStraight + RightLoStraight + leftLoUppercut + RightLoUppercut + clinchstrikesbody + leftBodyKick + RightBodyKick
    
    legtargeting = leftLegKick + RightLegKick
    
    totalthrown = headtargeting + bodytargeting + legtargeting
    
    try:
        headlandpercent = (headtargeting/totalthrown) * 100
    except:
        headlandpercent = 0
    
    
    headlandpercent = int(round(headlandpercent))
    
    try:
        bodylandpercent = (bodytargeting/totalthrown) * 100
    except:
        bodylandpercent = 0
    
    
    bodylandpercent = int(round(bodylandpercent))
    
    try:
        leglandpercent = (legtargeting/totalthrown) * 100
    except:
        leglandpercent = 0
    
    leglandpercent = int(round(leglandpercent))
    
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"HeadTargeting": str(headlandpercent) + '%'}})
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"BodyTargeting": str(bodylandpercent) + '%'}})
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"LegTargeting": str(leglandpercent) + '%'}})
    
    punchesabsorbed = JabsAbsorbed + StraightsAbsorbed + HooksAbsorbed + UppercutsAbsorbed
    puncheslanded = bothhands
    punchplusminus = puncheslanded - punchesabsorbed
    
    kicksabsorbed = BodyKicksAbsorbed + HeadKicksAbsorbed + LegKicksAbsorbed
    kickslanded = leftBodyKick + RightBodyKick + leftLegKick + RightLegKick + leftHighKick + RightHighKick
    kickplusminus = kickslanded - kicksabsorbed
    
    strikeplusminus = kickplusminus + punchplusminus
    
    
    
    
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"PunchPlusMinus": punchplusminus}})
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"KickPlusMinus": kickplusminus}})
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"StrikePlusMinus": strikeplusminus}})
    
    #Get Round by Round Stats
    total = round1strikes + round2strikes + round3strikes + round4strikes + round5strikes
    
    round1per = (round1strikes/total) * 100
    round1per = int(round(round1per))
    
    round2per = (round2strikes/total) * 100
    round2per = int(round(round2per))
    
    round3per = (round3strikes/total) * 100
    round3per = int(round(round3per))
    
    round4per = (round4strikes/total) * 100
    round4per = int(round(round4per))
    
    round5per = (round5strikes/total) * 100
    round5per = int(round(round5per))
    
    
    straightPunchesAbsorbed = JabsAbsorbed + StraightsAbsorbed
    loopingPunchesAbsorbed = HooksAbsorbed + OverhandsAbsorbed 
    totalloopstraightAbsorbed = straightPunchesAbsorbed + loopingPunchesAbsorbed
    
    
    try:
        straightPerAbs = (straightPunchesAbsorbed/totalloopstraightAbsorbed) * 100
    except:
        straightPerAbs = 0
    
    straightPerAbs = int(round(straightPerAbs))
    
    try:
        loopPerAbs = (loopingPunchesAbsorbed/totalloopstraightAbsorbed) * 100
    except:
        loopPerAbs = 0
    
    loopPerAbs = int(round(loopPerAbs))
    
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"straightPunchesAbs": str(straightPerAbs) + '%'}})
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"loopingPunchesAbs": str(loopPerAbs) + '%'}})
    
    
    straightPunches = leftjabhimake + leftjablomake + rightjabhimake + rightjablomake + leftstraighthimake + leftstraightlomake + rightstraighthimake + rightstraightlomake
    
    loopingPunches = lefthookhimake + lefthooklomake + righthookhimake + righthooklomake + leftOverhandMake + rightOverhandMake
    totalloopstraight = straightPunches + loopingPunches
    
    try:
        straightPer = (straightPunches/totalloopstraight) * 100
    except:
        straightPer = 0
    
    straightPer = int(round(straightPer))
    
    try:
        loopPer = (loopingPunches/totalloopstraight) * 100
    except:
        loopPer = 0
    
    loopPer = int(round(loopPer))
    
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"straightPunches": str(straightPer) + '%'}})
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"loopingPunches": str(loopPer) + '%'}})
    
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"Round1Output": str(round1per) + '%'}})
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"Round2Output": str(round2per) + '%'}})
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"Round3Output": str(round3per) + '%'}})
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"Round4Output": str(round4per) + '%'}})
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"Round5Output": str(round5per) + '%'}})
    
    min = minutesTracked
    totalStrikes = totalroundStrikes
    highImpactStrikes = totalStrikes - total20strikesmade
    highImpactStrikes = totalStrikes - (totalStrikes / 5)
    highImpactStrikes = highImpactStrikes * 2
    takedowns = singleLegTakedownAttempts + doubleLegTakedownAttempts + tripTakedownAttempts + throwTakedownAttempts + bodyLockTakedownAttempts
    
    
    highImpactAbs = (OverhandsAbsorbed + HooksAbsorbed + UppercutsAbsorbed + LegKicksAbsorbed + BodyKicksAbsorbed) / min
    lowImpactAbs = (JabsAbsorbed + HeadKicksAbsorbed + StraightsAbsorbed) / min
    
    
    
    
    try:
        offensiveRating = ((totalStrikes / min) * 25) + ((highImpactStrikes / min) * 25) + ((takedowns / min) * 25)
        offensiverating = offensiveRating / 3

        roundedor = round(offensiverating, 1)
        
        if roundedor > 182:
            roundedor = 182
        
    except:
        roundedor = 0
        
        
    try:
        fer = (roundedor - (highImpactAbs + lowImpactAbs)) / 3
        roundedfer = round(fer, 1)
    except:
        roundedfer = 0
        
    
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"offensiveRating": roundedor}})
    db.WEBFighterData.update_one({"fighterCode":y}, {"$set": {"fer": roundedfer}})
    
   
    

    
    
    
    
print("Done!")



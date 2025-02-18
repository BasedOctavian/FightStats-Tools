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
webnodatafighter = db["WEBFighterNoData"]





#Creating A Set To Hold All The Fighter Codes In Each Weight Class
heavyweightSet = set()
lightheavyweightSet = set()
middleweightSet = set()
welterweightSet = set()
lightweightSet = set()
featherweightSet = set()
bantamweightSet = set()
flyweightSet = set()
UsedSet = set()

allfighterset = set()

#Filter Arguments For Each Weight Class
allfightercodes = db.FighterNames.distinct('fighterCode')



for x in allfightercodes:
    
    imageurl = str()
    imageurl = ""
    
    imageurl = db.WEBFighterData.find({"fighterCode":x}, {"$exists": True}).distinct('Image')
    
    imageurl = str(imageurl)
    
    
    xox = db.WEBFighterData.find({"fighterCode":x}, {"Company":1, "_id":0}).distinct('Company')
    
    try:
        companyval = xox[0]
    except:
        companyval = "UFC"
    
    if companyval is None:
        company = 'UFC'
    else:
        company = companyval

    
    
    
    
    
    db.WEBFighterData.delete_one({"fighterCode":x})
    
    xox = db.FighterData.find({"fighterCode":x}, {"FightsTracked":1, "_id":0}).distinct('FightsTracked')
  
    
    fightsTracked = xox[0]
    
    xox = db.FighterData.find({"fighterCode":x}, {"RoundsTracked":1, "_id":0}).distinct('RoundsTracked')
    RoundsTracked = xox[0]
    
    
   
    
    
    if fightsTracked > 2 or RoundsTracked > 3:
        
        
        xox = db.FighterNames.find({"fighterCode":x}, {"fighterName":1, "_id":0}).distinct('fighterName')
        fighterName = xox[0]
        
        xox = db.FighterNames.find({"fighterCode":x}, {"nickname":1, "_id":0}).distinct('nickname')        
        nickname = xox[0]
        xox = db.FighterNames.find({"fighterCode":x}, {"gender":1, "_id":0}).distinct('gender') 
        gender = xox[0]
        xox = db.FighterNames.find({"fighterCode":x}, {"origin":1, "_id":0}).distinct('origin') 
        origin = xox[0]
        xox = db.FighterNames.find({"fighterCode":x}, {"origin":1, "_id":0}).distinct('height') 
        height = xox[0]
        xox = db.FighterNames.find({"fighterCode":x}, {"origin":1, "_id":0}).distinct('weight') 
        weight = xox[0]
        
        if weight == 115:
            weightname = "Womens Strawweight"
            
        if weight == 125 and gender == "Female":
            weightname = "Womens Flyweight"
            
        if weight == 135 and gender == "Female":
            weightname = "Womens Bantamweight"
            
        if weight == 145 and gender == "Female":
            weightname = "Womens Featherweight"
            
        if weight == 125 and gender == "Male":
            weightname = "Flyweight"
            
        if weight == 135 and gender == "Male":
            weightname = "Bantamweight"
            
        if weight == 145 and gender == "Male":
            weightname = "Featherweight"
            
        if weight == 155 and gender == "Male":
            weightname = "Lightweight"
            
        if weight == 170 and gender == "Male":
            weightname = "Welterweight"
            
        if weight == 185 and gender == "Male":
            weightname = "Middleweight"
            
        if weight == 205 and gender == "Male":
            weightname = "Light Heavyweight"
            
        if weight == 265 and gender == "Male":
            weightname = "Heavyweight"
        
        newurl = imageurl.replace("[", "")
        newurl2 = newurl.replace("]", "")
        newurl3 = newurl2.replace("'", "")
        newurl3 = newurl3.replace('"', '')
        
        
        
        
        
        
        #Gets Reach & Origin
        
        xox = db.WEBFighterNoData.find({"fighterName":fighterName}, {"fighterReach":1, "_id":0}).distinct('fighterReach') 
        
        try:
            newreach = xox[0]
            newreach = round(int(float(newreach)))
        except:
            newreach = ''
        
        xox = db.WEBFighterNoData.find({"fighterName":fighterName}, {"fighterLOC":1, "_id":0}).distinct('fighterLOC') 
        try:
            neworigin = xox[0]
        except:
            neworigin = ''
        
        #Gets W-L-D
       
        xox = db.WEBFighterNoData.find({"fighterName":fighterName}, {"wins":1, "_id":0}).distinct('wins') 
        if fighterName != 'Junior Dos Santos' and fighterName != 'Ovince Saint Preux' and fighterName != 'Rafael dos Anjos' and fighterName != 'Serghei Spivak' and fighterName != 'Alexey Oleynik' and fighterName != 'Chan Sung Jung':
            wins = xox[0]
        
        else:
            wins = 0
        
        
        xox = db.WEBFighterNoData.find({"fighterName":fighterName}, {"loss":1, "_id":0}).distinct('loss') 
        if fighterName != 'Junior Dos Santos' and fighterName != 'Ovince Saint Preux' and fighterName != 'Rafael dos Anjos' and fighterName != 'Serghei Spivak' and fighterName != 'Alexey Oleynik' and fighterName != 'Chan Sung Jung':
            loss = xox[0]
        else:
            loss = 0
        
        xox = db.WEBFighterNoData.find({"fighterName":fighterName}, {"loss":1, "_id":0}).distinct('draw') 
        if fighterName != 'Junior Dos Santos' and fighterName != 'Ovince Saint Preux' and fighterName != 'Rafael dos Anjos' and fighterName != 'Serghei Spivak' and fighterName != 'Alexey Oleynik' and fighterName != 'Chan Sung Jung':
            draw = xox[0]
        else:
            draw = 0
        
        
        fighterfights = "https://www.fightstats.xyz/search?q=" + fighterName
        
        mydict = { 
                "fighterCode": x,
                "fighterName": fighterName,
                "nickname": nickname,
                "wins": wins,
                "loss": loss,
                "draw": draw,
                "gender": gender,
                "origin": neworigin,
                "height": height,
                "weight": weightname,
                "reach": newreach,
                "Image": newurl3,
                "Company": company,
                "TakedownRate": "",
                "TakedownRateAV": "",
                "SingleLegsPer25": 0,
                "DoubleLegsPer25": 0,
                "TripsPer25": 0,
                "BodyLocksPer25": 0,
                "ThrowsPer25": 0,
                "TimesSingleLegsPer25": 0,
                "TimesDoubleLegsPer25": 0,
                "TimesTripsPer25": 0,
                "TimesBodyLocksPer25": 0,
                "TimesThrowsPer25": 0,
                "StrikeLandRate": "",
                "StrikeLandRateAV": "",
                "KickLandRate": "",
                "KickLandRateAV": "",
                "PunchLandRate": "",
                "PunchLandRateAV": "",
                "KnockdownsPer25": 0,
                "KnockdownsPer25AV": 0,
                "StunsPer25": 0,
                "StunsPer25AV": 0,
                "TimesStunnedPer25": 0,
                "TimesStunnedPer25AV": 0,
                "TimesKnockedDownPer25": 0,
                "TimesKnockedDownPer25AV": 0,
                "SubAttemptsPer25": 0,
                "SubAttemptsPer25AV": 0,
                "1StrikeLanded": "",
                "2StrikeLanded": "",
                "3StrikeLanded": "",
                "1StrikeAbsorbed": "",
                "2StrikeAbsorbed": "",
                "3StrikeAbsorbed": "",
                "1CagePosition": "",
                "1TopCombo": "",
                "2TopCombo": "",
                "3TopCombo": "",
                "1Stance": "",
                "RecordAgainstSwitch": "",
                "RecordAgainstOrthodox": "",
                "RecordAgainstSouthpaw": "",
                "FightsTracked": fightsTracked,
                "RoundsTracked": 0,
                "MinutesTracked": 0,
                "Round1StrikesLanded": 0,
                "Round2StrikesLanded": 0,
                "Round3StrikesLanded": 0,
                "Round4StrikesLanded": 0,
                "Round5StrikesLanded": 0,
                "FighterGrade": 0,
                "StrikingGrade": 0,
                "KickingGrade": 0,
                "GrapplingGrade": 0,
                "DefensiveGrade": 0,
                "ChinGrade": 0,
                "LastFighterGrade": 0,
                "LeftJabHiMake": 0,
                "LeftJabLoMake": 0,
                "RightJabHiMake": 0,
                "RightJabLoMake": 0,
                "LeftStraightHiMake": 0,
                "LeftStraightLoMake": 0,
                "RightStraightHiMake": 0,
                "RightStraightLoMake": 0,
                "LeftHookHiMake": 0,
                "LeftHookLoMake": 0,
                "RightHookHiMake": 0,
                "RightHookLoMake": 0,
                "LeftOverhandMake": 0,
                "RightOverhandMake": 0,
                "TotalGroundStrikesToTheHead": 0,
                "TotalGroundStrikesToTheBody": 0,
                "TotalClinchStrikesToTheHead": 0,
                "TotalClinchStrikesToTheBody": 0,
                "TotalElbows": 0,
                "StrikesLPM": 0,
                "StrikesTPM": 0,
                "PunchesLPM": 0,
                "PunchesTPM": 0,
                "KicksLPM": 0,
                "KicksTPM": 0,
                "punchapm": 0,
                "kickapm": 0,
                "strikeapm": 0,
                "strikingGameplans": 0,
                "grapplingGameplans": 0,
                "standingPOSStrikes": 0,
                "clinchPOSStrikes": 0,
                "groundPOSStrikes": 0,
                "TDDefense": 0,
                "HighImpactDropPercent": 0,
                "HighImpactStunPercent": 0,
                "HighImpactDroppedPercent": 0,
                "HighImpactStunnedPercent": 0,
                "LeftHandThrowPercent": 0,
                "RightHandThrowPercent": 0,
                "HeadTargeting": 0,
                "BodyTargeting": 0,
                "LegTargeting": 0,
                "StrikePlusMinus": 0,
                "PunchPlusMinus": 0,
                "KickPlusMinus": 0,
                "HighImpactStrikePercent": 0,
                "LowImpactStrikePercent": 0,
                "Round1Output": 0,
                "Round2Output": 0,
                "Round3Output": 0,
                "Round4Output": 0,
                "Round5Output": 0,
                "LeftHandABS": 0,
                "RightHandABS": 0,
                "HeadABS": 0,
                "BodyABS": 0,
                "LegABS": 0,
                "LeftHiKick": 0,
                "RightHiKick": 0,
                "LeftBodyKick": 0,
                "RightBodyKick": 0,
                "LeftLegKick": 0,
                "RightLegKick": 0,
                "loopingPunches": 0,
                "straightPunches": 0,
                "straightPunchesAbs": 0,
                "loopingPunchesAbs": 0,
                "OrthodoxOppJabs": 0,
                "OrthodoxOppStraights": 0,
                "OrthodoxOppHooks": 0,
                "OrthodoxOppUppercuts": 0,
                "OrthodoxOppLegKicks": 0,
                "OrthodoxOppBodyKicks": 0,
                "OrthodoxOppHeadKicks": 0,
                "OrthodoxOppOverhands": 0,
                "SouthpawOppJabs": 0,
                "SouthpawOppStraights": 0,
                "SouthpawOppHooks": 0,
                "SouthpawOppUppercuts": 0,
                "SouthpawOppLegKicks": 0,
                "SouthpawOppBodyKicks": 0,
                "SouthpawOppHeadKicks": 0,
                "SouthpawOppOverhands": 0,
                "SwitchOppJabs": 0,
                "SwitchOppStraights": 0,
                "SwitchOppHooks": 0,
                "SwitchOppUppercuts": 0,
                "SwitchOppLegKicks": 0,
                "SwitchOppBodyKicks": 0,
                "SwitchOppHeadKicks": 0,
                "SwitchOppOverhands": 0,
                "offensiveRating": 0,
                "fer": 0,
                "searchFights": fighterfights
                }
            
        
        webfighterdata.insert_one(mydict)
        
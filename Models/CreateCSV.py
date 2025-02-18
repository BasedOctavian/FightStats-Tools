#Figures out the average stats per each weight class 
import pymongo
import csv
import sqlite3
import random



#Setting Up The Connections To The DB
myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@octc1.d2he2mx.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]

#Stance Nominal Vars
#Orthodox = 0
#Southpaw = 1
#Switch = 2

#Styles
#Striker = 0
#Grappler = 1
#Balanced = 2
flipit = 0

#Gets All Of The Fights In The Main DB
allfightcodes = db.Fights.distinct('fightCode')

#Gets All The Fighters In The Website
allwebfighters = db.WEBFighterData.distinct('fighterCode')

runcounter = 0

for x in allfightcodes:
        
        doesafighterexist = False
        doesbfighterexist = False
        
        #Does at least one fighter exist within this fight
        
        xox = db.Fights.find({"fightCode":x}, {"fighterB":1, "_id":0}).distinct('fighterB')
        fighterb = xox[0]
        xox = db.Fights.find({"fightCode":x}, {"fighterA":1, "_id":0}).distinct('fighterA')
        fightera = xox[0]
        
        doesafighterexist = False
        for y in allwebfighters:
            if y == fightera:
                doesafighterexist = True
            if y == fighterb:
                doesbfighterexist = True
            
        
        
        if doesafighterexist == True and doesbfighterexist == True:
            
            if flipit > 1:
                tempa = fightera
                tempb = fighterb
                fightera = tempb
                fighterb = tempa
                flipit = 0
                Winner = 1
            else:
                Winner = 0
            
            #Begin Grabbing the data
            xox = db.FighterData.find({"fighterCode":fightera}, {"MinutesTracked":1, "_id":0}).distinct('MinutesTracked')
            fighteramin = xox[0]
            xox = db.FighterData.find({"fighterCode":fighterb}, {"MinutesTracked":1, "_id":0}).distinct('MinutesTracked')
            fighterbmin = xox[0]
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"1Stance":1, "_id":0}).distinct('1Stance')

            if xox[0] == "Orthodox":
                AOrthodox = 1
                ASouthpaw = 0
                ASwitch = 0
                
            if xox[0] == "Southpaw":
                AOrthodox = 0
                ASouthpaw = 1
                ASwitch = 0
                
            if xox[0] == "Orthodox":
                AOrthodox = 1
                ASouthpaw = 0
                ASwitch = 0
                
            if xox[0] == "Switch":
                AOrthodox = 0
                ASouthpaw = 0
                ASwitch = 1
                
            print(fighterb)   
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"1Stance":1, "_id":0}).distinct('1Stance')

            if xox[0] == "Orthodox":
                BOrthodox = 1
                BSouthpaw = 0
                BSwitch = 0
                
            if xox[0] == "Southpaw":
                BOrthodox = 0
                BSouthpaw = 1
                BSwitch = 0
                
            if xox[0] == "Orthodox":
                BOrthodox = 1
                BSouthpaw = 0
                BSwitch = 0
                
            if xox[0] == "Switch":
                BOrthodox = 0
                BSouthpaw = 0
                BSwitch = 1
        
        
        
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"SingleLegsPer25":1, "_id":0}).distinct('SingleLegsPer25')  
            ATakedownsPer25 = xox[0]
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"DoubleLegsPer25":1, "_id":0}).distinct('DoubleLegsPer25')  
            ATakedownsPer25 = xox[0] + ATakedownsPer25
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"TripsPer25":1, "_id":0}).distinct('TripsPer25')  
            ATakedownsPer25 = xox[0] + ATakedownsPer25
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"ThrowsPer25":1, "_id":0}).distinct('ThrowsPer25')  
            ATakedownsPer25 = xox[0] + ATakedownsPer25
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"BodyLocksPer25":1, "_id":0}).distinct('BodyLocksPer25')  
            ATakedownsPer25 = xox[0] + ATakedownsPer25
            
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"SingleLegsPer25":1, "_id":0}).distinct('SingleLegsPer25')  
            BTakedownsPer25 = xox[0]
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"DoubleLegsPer25":1, "_id":0}).distinct('DoubleLegsPer25')  
            BTakedownsPer25 = xox[0] + BTakedownsPer25
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"TripsPer25":1, "_id":0}).distinct('TripsPer25')  
            BTakedownsPer25 = xox[0] + BTakedownsPer25
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"ThrowsPer25":1, "_id":0}).distinct('ThrowsPer25')  
            BTakedownsPer25 = xox[0] + BTakedownsPer25
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"BodyLocksPer25":1, "_id":0}).distinct('BodyLocksPer25')  
            BTakedownsPer25 = xox[0] + BTakedownsPer25
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"ChinGrade":1, "_id":0}).distinct('ChinGrade')  
            AChinGrade = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"ChinGrade":1, "_id":0}).distinct('ChinGrade')  
            BChinGrade = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"DefensiveGrade":1, "_id":0}).distinct('DefensiveGrade')  
            ADefensiveGrade = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"DefensiveGrade":1, "_id":0}).distinct('DefensiveGrade')  
            BDefensiveGrade = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"FighterGrade":1, "_id":0}).distinct('FighterGrade')  
            AFighterGrade = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"FighterGrade":1, "_id":0}).distinct('FighterGrade')  
            BFighterGrade = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"FightsTracked":1, "_id":0}).distinct('FightsTracked')  
            AFightsTracked = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"FightsTracked":1, "_id":0}).distinct('FightsTracked')  
            BFightsTracked = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"GrapplingGrade":1, "_id":0}).distinct('GrapplingGrade')  
            AGrapplingGrade = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"GrapplingGrade":1, "_id":0}).distinct('GrapplingGrade')  
            BGrapplingGrade = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"StrikingGrade":1, "_id":0}).distinct('StrikingGrade')  
            AStrikingGrade = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"StrikingGrade":1, "_id":0}).distinct('StrikingGrade')  
            BStrikingGrade = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"KnockdownsPer25":1, "_id":0}).distinct('KnockdownsPer25')  
            AKnockdownsPer25 = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"KnockdownsPer25":1, "_id":0}).distinct('KnockdownsPer25')  
            BKnockdownsPer25 = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"StunsPer25":1, "_id":0}).distinct('StunsPer25')  
            AStunsPer25 = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"StunsPer25":1, "_id":0}).distinct('StunsPer25')  
            BStunsPer25 = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"SubAttemptsPer25":1, "_id":0}).distinct('SubAttemptsPer25')  
            ASubAttemptsPer25 = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"SubAttemptsPer25":1, "_id":0}).distinct('SubAttemptsPer25')  
            BSubAttemptsPer25 = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"TimesKnockedDownPer25":1, "_id":0}).distinct('TimesKnockedDownPer25')  
            ATimesKnockedDownPer25 = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"TimesKnockedDownPer25":1, "_id":0}).distinct('TimesKnockedDownPer25')  
            BTimesKnockedDownPer25 = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"TimesStunnedPer25":1, "_id":0}).distinct('TimesStunnedPer25')  
            ATimesStunnedPer25 = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"TimesStunnedPer25":1, "_id":0}).distinct('TimesStunnedPer25')  
            BTimesStunnedPer25 = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"StrikesLPM":1, "_id":0}).distinct('StrikesLPM')  
            AStrikesLandedPerMin = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"StrikesLPM":1, "_id":0}).distinct('StrikesLPM')  
            BStrikesLandedPerMin = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"StrikesTPM":1, "_id":0}).distinct('StrikesTPM')  
            AStrikesThrownPerMin = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"StrikesTPM":1, "_id":0}).distinct('StrikesTPM')  
            BStrikesThrownPerMin = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"PunchesLPM":1, "_id":0}).distinct('PunchesLPM')  
            APunchesLandedPerMin = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"PunchesLPM":1, "_id":0}).distinct('PunchesLPM')  
            BPunchesLandedPerMin = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"PunchesTPM":1, "_id":0}).distinct('PunchesTPM')  
            APunchesThrownPerMin = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"PunchesTPM":1, "_id":0}).distinct('PunchesTPM')  
            BPunchesThrownPerMin = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"KicksLPM":1, "_id":0}).distinct('KicksLPM')  
            AKicksLandedPerMin = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"KicksLPM":1, "_id":0}).distinct('KicksLPM')  
            BKicksLandedPerMin = xox[0]
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"KicksTPM":1, "_id":0}).distinct('KicksTPM')  
            AKicksThrownPerMin = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"KicksTPM":1, "_id":0}).distinct('KicksTPM')  
            BKicksThrownPerMin = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"kickapm":1, "_id":0}).distinct('kickapm')  
            AKicksAbsorbedPerMin = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"kickapm":1, "_id":0}).distinct('kickapm')  
            BKicksAbsorbedPerMin = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"punchapm":1, "_id":0}).distinct('punchapm')  
            APunchesAbsorbedPerMin = xox[0] 
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"punchapm":1, "_id":0}).distinct('punchapm')  
            BPunchesAbsorbedPerMin = xox[0] 
            
            
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"TimesSingleLegsPer25":1, "_id":0}).distinct('TimesSingleLegsPer25')  
            ATimesTakendownPer25 = xox[0]
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"TimesDoubleLegsPer25":1, "_id":0}).distinct('TimesDoubleLegsPer25')  
            ATimesTakendownPer25 = xox[0] + ATimesTakendownPer25
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"TimesTripsPer25":1, "_id":0}).distinct('TimesTripsPer25')  
            ATimesTakendownPer25 = xox[0] + ATimesTakendownPer25
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"TimesThrowsPer25":1, "_id":0}).distinct('TimesThrowsPer25')  
            ATimesTakendownPer25 = xox[0] + ATimesTakendownPer25
            
            xox = db.WEBFighterData.find({"fighterCode":fightera}, {"TimesBodyLocksPer25":1, "_id":0}).distinct('TimesBodyLocksPer25')  
            ATimesTakendownPer25 = xox[0] + ATimesTakendownPer25
            
            
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"TimesSingleLegsPer25":1, "_id":0}).distinct('TimesSingleLegsPer25')  
            BTimesTakendownPer25 = xox[0]
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"TimesDoubleLegsPer25":1, "_id":0}).distinct('TimesDoubleLegsPer25')  
            BTimesTakendownPer25 = xox[0] + BTimesTakendownPer25
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"TimesTripsPer25":1, "_id":0}).distinct('TimesTripsPer25')  
            BTimesTakendownPer25 = xox[0] + BTimesTakendownPer25
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"TimesThrowsPer25":1, "_id":0}).distinct('TimesThrowsPer25')  
            BTimesTakendownPer25 = xox[0] + BTimesTakendownPer25
            
            xox = db.WEBFighterData.find({"fighterCode":fighterb}, {"TimesBodyLocksPer25":1, "_id":0}).distinct('TimesBodyLocksPer25')  
            BTimesTakendownPer25 = xox[0] + BTimesTakendownPer25
            
            xox = db.FighterData.find({"fighterCode":fightera}, {"StrikingGameplans":1, "_id":0}).distinct('StrikingGameplans')  
            astrgp = xox[0]
            xox = db.FighterData.find({"fighterCode":fightera}, {"GrapplingGameplans":1, "_id":0}).distinct('GrapplingGameplans')  
            agrpgp = xox[0]
            
            AStyle = 2
            
            if astrgp > agrpgp:
                AStyle = 0
            
            else:
                AStyle = 1
                
                
                
            xox = db.FighterData.find({"fighterCode":fighterb}, {"StrikingGameplans":1, "_id":0}).distinct('StrikingGameplans')  
            bstrgp = xox[0]
            xox = db.FighterData.find({"fighterCode":fighterb}, {"GrapplingGameplans":1, "_id":0}).distinct('GrapplingGameplans')  
            bgrpgp = xox[0]
            
            BStyle = 2
            
            if bstrgp > bgrpgp:
                BStyle = 0
            
            else:
                BStyle = 1
                
            AOdds = 0
            BOdds = 0
            
            xox = db.FighterNames.find({"fighterCode":fightera}, {"fighterName":1, "_id":0}).distinct('fighterName')
            AName = xox[0]
            
            xox = db.FighterNames.find({"fighterCode":fighterb}, {"fighterName":1, "_id":0}).distinct('fighterName')
            BName = xox[0]
            
            flipit = flipit + 1
            
            

            column_name = ["AOrthodox", 
                        "ASouthpaw", 
                        "ASwitch",
                        "ATakedownsPer25",
                        "ATimesTakendownPer25",
                        "AChinGrade",
                        "ADefensiveGrade", 
                        "AFighterGrade",
                        "AFightsTracked",
                        "AGrapplingGrade",
                        "AStrikingGrade",
                        "AKnockdownsPer25",
                        "AStunsPer25",
                        "ASubAttemptsPer25",
                        "ATimesKnockedDownPer25",
                        "ATimesStunnedPer25",
                        "AStrikesLandedPerMin",
                        "AStrikesThrownPerMin",
                        "APunchesLandedPerMin",
                        "APunchesThrownPerMin",
                        "AKicksLandedPerMin",
                        "AKicksThrownPerMin",
                        "AKicksAbsorbedPerMin",
                        "APunchesAbsorbedPerMin",
                        "BOrthodox", 
                        "BSouthpaw", 
                        "BSwitch",
                        "BTakedownsPer25",
                        "BTimesTakendownPer25",
                        "BChinGrade",
                        "BDefensiveGrade", 
                        "BFighterGrade",
                        "BFightsTracked",
                        "BGrapplingGrade",
                        "BStrikingGrade",
                        "BKnockdownsPer25",
                        "BStunsPer25",
                        "BSubAttemptsPer25",
                        "BTimesKnockedDownPer25",
                        "BTimesStunnedPer25",
                        "BStrikesLandedPerMin",
                        "BStrikesThrownPerMin",
                        "BPunchesLandedPerMin",
                        "BPunchesThrownPerMin",
                        "BKicksLandedPerMin",
                        "BKicksThrownPerMin",
                        "BKicksAbsorbedPerMin",
                        "BPunchesAbsorbedPerMin",
                        "AStyle",
                        "BStyle",
                        "AOdds",
                        "BOdds",
                        "Winner",
                        "AName",
                        "BName",
                        ] #The name of the columns



            data = [    AOrthodox, 
                        ASouthpaw, 
                        ASwitch,
                        ATakedownsPer25,
                        ATimesTakendownPer25,
                        AChinGrade,
                        ADefensiveGrade, 
                        AFighterGrade,
                        AFightsTracked,
                        AGrapplingGrade,
                        AStrikingGrade,
                        AKnockdownsPer25,
                        AStunsPer25,
                        ASubAttemptsPer25,
                        ATimesKnockedDownPer25,
                        ATimesStunnedPer25,
                        AStrikesLandedPerMin,
                        AStrikesThrownPerMin,
                        APunchesLandedPerMin,
                        APunchesThrownPerMin,
                        AKicksLandedPerMin,
                        AKicksThrownPerMin,
                        AKicksAbsorbedPerMin,
                        APunchesAbsorbedPerMin,
                        BOrthodox, 
                        BSouthpaw, 
                        BSwitch,
                        BTakedownsPer25,
                        BTimesTakendownPer25,
                        BChinGrade,
                        BDefensiveGrade, 
                        BFighterGrade,
                        BFightsTracked,
                        BGrapplingGrade,
                        BStrikingGrade,
                        BKnockdownsPer25,
                        BStunsPer25,
                        BSubAttemptsPer25,
                        BTimesKnockedDownPer25,
                        BTimesStunnedPer25,
                        BStrikesLandedPerMin,
                        BStrikesThrownPerMin,
                        BPunchesLandedPerMin,
                        BPunchesThrownPerMin,
                        BKicksLandedPerMin,
                        BKicksThrownPerMin,
                        BKicksAbsorbedPerMin,
                        BPunchesAbsorbedPerMin,
                        AStyle,
                        BStyle,
                        AOdds,
                        BOdds,
                        Winner,
                        AName,
                        BName,] 
            if runcounter == 0:
                
                with open('model.csv', 'w') as f:
                    writer = csv.writer(f) #this is the writer object
                    writer.writerow(column_name) # this will list out the names of the columns which are always the first entrries
                    writer.writerow(data) #this is the data
                    
            if runcounter > 0:
                
                with open('model.csv', 'a') as f:
                    writer = csv.writer(f) #this is the writer object
                    writer.writerow(data) #this is the data    
                
            runcounter = runcounter + 1
#Figures out the average stats per each weight class 
import pymongo
import csv
import sqlite3

from AAV import *

#Setting Up The Connections To The DB
myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@octc1.d2he2mx.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]
fighterdata = db["FighterData"]
fighternames = db["FighterNames"]
weightclasses = db["WeightClasses"]

#Creating A Set To Hold All The Fighter Codes In Each Weight Class
heavyweightSet = set()
lightheavyweightSet = set()
middleweightSet = set()
welterweightSet = set()
lightweightSet = set()
featherweightSet = set()
bantamweightSet = set()
flyweightSet = set()
strawweightSet = set()
UsedSet = set()

#Filter Arguments For Each Weight Class
heavyweightnamedoc = db.FighterNames.find({"weight":265},{"fighterCode":1,  "_id":0}).distinct('fighterCode');
lightheavyweightnamedoc = db.FighterNames.find({"weight":205},{"fighterCode":1,  "_id":0}).distinct('fighterCode');
middleweightnamedoc = db.FighterNames.find({"weight":185},{"fighterCode":1,  "_id":0}).distinct('fighterCode');
welterweightnamedoc = db.FighterNames.find({"weight":170},{"fighterCode":1,  "_id":0}).distinct('fighterCode');
lightweightnamedoc = db.FighterNames.find({"weight":155},{"fighterCode":1,  "_id":0}).distinct('fighterCode');
featherweightnamedoc = db.FighterNames.find({"weight":145},{"fighterCode":1,  "_id":0}).distinct('fighterCode');
bantamweightnamedoc = db.FighterNames.find({"weight":135},{"fighterCode":1,  "_id":0}).distinct('fighterCode');
flyweightnamedoc = db.FighterNames.find({"weight":125},{"fighterCode":1,  "_id":0}).distinct('fighterCode');
strawweightnamedoc = db.FighterNames.find({"weight":115},{"fighterCode":1,  "_id":0}).distinct('fighterCode');


#Adds All The Fighters From Each Weight Class To A WC Specific Set
if weightnum == 265:
    for x in heavyweightnamedoc:
        if x not in heavyweightSet:
            heavyweightSet.add(x)
      
if weightnum == 205:        
    for x in lightheavyweightnamedoc:
        if x not in lightheavyweightSet:
            lightheavyweightSet.add(x)

if weightnum == 185:     
    for x in middleweightnamedoc:
        if x not in middleweightSet:
            middleweightSet.add(x)

if weightnum == 170:        
    for x in welterweightnamedoc:
        if x not in welterweightSet:
            welterweightSet.add(x)

if weightnum == 155:
    for x in lightweightnamedoc:
        if x not in lightweightSet:
            lightweightSet.add(x)

if weightnum == 145:        
    for x in featherweightnamedoc:
        if x not in featherweightSet:
            featherweightSet.add(x)

if weightnum == 135:      
    for x in bantamweightnamedoc:
        if x not in bantamweightSet:
            bantamweightSet.add(x)

if weightnum == 125:   
    for x in flyweightnamedoc:
        if x not in flyweightSet:
            flyweightSet.add(x)
            
if weightnum == 115:   
    for x in strawweightnamedoc:
        if x not in strawweightSet:
            strawweightSet.add(x)
        
        
weightclass = int()



#Create All The WC Specific Average Variables
minutes = int()
rounds = int()
fights = int()


kowins = int()
tkowins = int()
tkoloss = int()
koloss = int()
subwin = int()
subloss = int()
decwin = int()
decloss = int()
subattempt = int()
timesknockeddown = int()
numberofknockdowns = int()
timesstunned = int()
numberofstuns = int()
AmericanaAttempts = int() 
AnacondaAttempt = int()
AttemptedThrowTD = int()	
BodyKicksAbsorbed = int()	
BodyLockTakedownAttempts = int()	
BulldogAttempt = int()	
CalfSlicerAttempts = int()	
ClinchStrikeHiMake	 = int()	
ClinchStrikeLoMake	 = int()
DoubleLegTakedownAttempts	 = int()
EzekielAttempt	 = int()
GogoplataAttempts		 = int()
GroundStrikeHiMake	 = int()
GroundStrikeLoMake	 = int()
HeadKicksAbsorbed	 = int()
HooksAbsorbed	 = int()
JabsAbsorbed	 = int()
KneebarAttempt		 = int()
LeftBodyKickMake	 = int()
LeftElbowMake	 = int()
LeftHighKickMake	 = int()
LeftHookHiMake	 = int()
LeftHookLoMake	 = int()
LeftJabHiMake	 = int()
LeftJabLoMake	 = int()
LeftLegKickMake	 = int()
LeftOverhandMake	 = int()
LeftSpinBackFistMake	 = int()
LeftStraightHiMake	 = int()
LeftStraightLoMake	 = int()
LeftUppercutHiMake	 = int()
LeftUppercutLoMake	 = int()
LegKicksAbsorbed	 = int()
LeglockAttempt	 = int()
LossesVsOrthodox	 = int()
LossesVsSouthpaw	 = int()
LossesVsSwitch	 = int()
NeckCrankAttempt	 = int()
OmoplataAttempt	 = int()
OtherSubAttempt	 = int()
OverhandsAbsorbed	 = int()
RightBodyKickMake	 = int()
RightElbowMake	 = int()
RightHighKickMake	 = int()
RightHookHiMake	 = int()
RightHookLoMake	 = int()
RightJabHiMake	 = int()
RightJabLoMake	 = int()
RightLegKickMake	 = int()
RightOverhandMake	 = int()
RightSpinBackFistMake	 = int()
RightStraightHiMake	 = int()
RightStraightLoMake	 = int()
RightUppercutHiMake	 = int()
RightUppercutLoMake	 = int()
SUBRNCAttempt	 = int()
SingleLegTakedownAttempts  = int()		
StraightsAbsorbed	 = int()
SubArmTriangleAttempt	 = int()
SubAttempts	 = int()
SubDarceAttempt	 = int()
SubGuillotineAttempt	 = int()
SubHeelHookAttempt	 = int()
SubKimuraAttempt	 = int()
SubNeckCrankAttempt	 = int()
SubStraightArmLockAttempt	 = int()
SubSulovStretchAttempt	 = int()
SubTriangleArmbarAttempt	 = int()
SubTriangleAttempt	 = int()
TotalBodyKicksMade	 = int()
TotalBodyKicksThrown	 = int()
TotalClinchStrikesMade	 = int()
TotalClinchStrikesThrown	 = int()
TotalElbowsMade = int()
TotalElbowsThrown	 = int()
TotalGroundStrikesMade = int()
TotalGroundStrikesThrown	 = int()
TotalHighKicksMade = int()
TotalHighKicksThrown	 = int()
TotalHooksMade = int()
TotalHooksThrown	 = int()
TotalJabsMade = int()
TotalJabsThrown	 = int()
TotalKicksLanded	 = int()
TotalKicksThrown	 = int()
TotalLegKicksMade	 = int()
TotalLegKicksThrown	 = int()
TotalOverhandsMade	 = int()
TotalOverhandsThrown = int()
TotalPunchesLanded	 = int()
TotalPunchesThrown	 = int()
TotalSpinBackFistsMade	 = int()
TotalSpinBackFistsThrown	 = int()
TotalStraightsMade	 = int()
TotalStraightsThrown	 = int()
TotalStrikesLanded	 = int()
TotalUppercutsMade	 = int()
TotalUppercutsThrown	 = int()
TripTakedownAttempts	 = int()
TwisterAttempts	 = int()
UppercutsAbsorbed	 = int()
VonFlueAttempt	 = int()
WinsVsOrthodox	 = int()
WinsVsSouthpaw	 = int()
WinsVsSwitch	 = int()











#Add each value from each fighter in each WC to a WC var
if weightnum == 265 :
    UsedSet = heavyweightSet
    
if weightnum == 205 :
    UsedSet = lightheavyweightSet

if weightnum == 185 :
    UsedSet = middleweightSet

if weightnum == 170 :
    UsedSet = welterweightSet
    
if weightnum == 155 :
    UsedSet = lightweightSet
    
if weightnum == 145 :
    UsedSet = featherweightSet
    
if weightnum == 135 :
    UsedSet = bantamweightSet
    
if weightnum == 125 :
    UsedSet = flyweightSet
    
if weightnum == 115 :
    UsedSet = strawweightSet
    



       
for y in UsedSet:
        #Gets The Minutes Tracked For The Current Fighter Iteration
        l = db.FighterData.find({"fighterCode":y},{"MinutesTracked":1,  "_id":0}).distinct('MinutesTracked');
        #Adds The Minutes For That Fighter To The Corresponding Mongo Collection
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"minutes": l[0]}})
        
        
        l = db.FighterData.find({"fighterCode":y},{"RoundsTracked":1,  "_id":0}).distinct('RoundsTracked');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"rounds": l[0]}})
        
        l = db.FighterData.find({"fighterCode":y},{"FightsTracked":1,  "_id":0}).distinct('FightsTracked');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"fights": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"FighterKOWins":1,  "_id":0}).distinct('FighterKOWins');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"kowins": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"FighterTKOWins":1,  "_id":0}).distinct('FighterTKOWins');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"tkowins": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"FighterTKOLoss":1,  "_id":0}).distinct('FighterTKOLoss');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"tkoloss": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"FighterKOLoss":1,  "_id":0}).distinct('FighterKOLoss');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"koloss": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"FighterSUBWin":1,  "_id":0}).distinct('FighterSUBWin');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"subwin": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"FighterSUBLoss":1,  "_id":0}).distinct('FighterSUBLoss');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"subloss": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"FighterUDWins":1,  "_id":0}).distinct('FighterUDWins');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"decwin": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"FighterMajDecWin":1,  "_id":0}).distinct('FighterMajDecWin');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"decwin": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"FighterSplitDecWin":1,  "_id":0}).distinct('FighterSplitDecWin');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"decwin": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"FighterUDLoss":1,  "_id":0}).distinct('FighterUDLoss');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"decloss": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"FighterMajDecLoss":1,  "_id":0}).distinct('FighterMajDecLoss');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"decloss": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"FighterSplitDecLoss":1,  "_id":0}).distinct('FighterSplitDecLoss');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"decloss": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"SubAttempts":1,  "_id":0}).distinct('SubAttempts');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"subattempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TimesKnockedDown":1,  "_id":0}).distinct('TimesKnockedDown');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"timesknockeddown": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"NumberOfKnockDowns":1,  "_id":0}).distinct('NumberOfKnockDowns');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"numberofknockdowns": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TimesStunned":1,  "_id":0}).distinct('TimesStunned');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"timesstunned": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"NumberOfStuns":1,  "_id":0}).distinct('NumberOfStuns');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"numberofstuns": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"AmericanaAttempts":1,  "_id":0}).distinct('AmericanaAttempts');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"AmericanaAttempts": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"AnacondaAttempt":1,  "_id":0}).distinct('AnacondaAttempt');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"AnacondaAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"AttemptedThrowTD":1,  "_id":0}).distinct('AttemptedThrowTD');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"AttemptedThrowTD": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"BodyKicksAbsorbed":1,  "_id":0}).distinct('BodyKicksAbsorbed');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"BodyKicksAbsorbed": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"BodyLockTakedownAttempts":1,  "_id":0}).distinct('BodyLockTakedownAttempts');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"BodyLockTakedownAttempts": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"BulldogAttempt":1,  "_id":0}).distinct('BulldogAttempt');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"BulldogAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"CalfSlicerAttempts":1,  "_id":0}).distinct('CalfSlicerAttempts');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"CalfSlicerAttempts": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"ClinchStrikeHiMake":1,  "_id":0}).distinct('ClinchStrikeHiMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"ClinchStrikeHiMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"ClinchStrikeLoMake":1,  "_id":0}).distinct('ClinchStrikeLoMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"ClinchStrikeLoMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"DoubleLegTakedownAttempts":1,  "_id":0}).distinct('DoubleLegTakedownAttempts');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"DoubleLegTakedownAttempts": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"EzekielAttempt":1,  "_id":0}).distinct('EzekielAttempt');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"EzekielAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"GogoplataAttempts":1,  "_id":0}).distinct('GogoplataAttempts');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"GogoplataAttempts": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"GroundStrikeHiMake":1,  "_id":0}).distinct('GroundStrikeHiMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"GroundStrikeHiMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"GroundStrikeLoMake":1,  "_id":0}).distinct('GroundStrikeLoMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"GroundStrikeLoMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"HeadKicksAbsorbed":1,  "_id":0}).distinct('HeadKicksAbsorbed');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"HeadKicksAbsorbed": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"HooksAbsorbed":1,  "_id":0}).distinct('HooksAbsorbed');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"HooksAbsorbed": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"JabsAbsorbed":1,  "_id":0}).distinct('JabsAbsorbed');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"JabsAbsorbed": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"KneebarAttempt":1,  "_id":0}).distinct('KneebarAttempt');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"KneebarAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"LeftBodyKickMake":1,  "_id":0}).distinct('LeftBodyKickMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"LeftBodyKickMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"LeftElbowMake":1,  "_id":0}).distinct('LeftElbowMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"LeftElbowMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"LeftHighKickMake":1,  "_id":0}).distinct('LeftHighKickMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"LeftHighKickMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"LeftHookHiMake":1,  "_id":0}).distinct('LeftHookHiMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"LeftHookHiMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"LeftHookLoMake":1,  "_id":0}).distinct('LeftHookLoMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"LeftHookLoMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"LeftJabHiMake":1,  "_id":0}).distinct('LeftJabHiMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"LeftJabHiMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"LeftJabLoMake":1,  "_id":0}).distinct('LeftJabLoMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"LeftJabLoMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"LeftLegKickMake":1,  "_id":0}).distinct('LeftLegKickMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"LeftLegKickMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"LeftOverhandMake":1,  "_id":0}).distinct('LeftOverhandMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"LeftOverhandMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"LeftSpinBackFistMake":1,  "_id":0}).distinct('LeftSpinBackFistMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"LeftSpinBackFistMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"LeftStraightHiMake":1,  "_id":0}).distinct('LeftStraightHiMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"LeftStraightHiMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"LeftStraightLoMake":1,  "_id":0}).distinct('LeftStraightLoMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"LeftStraightLoMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"LeftUppercutHiMake":1,  "_id":0}).distinct('LeftUppercutHiMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"LeftUppercutHiMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"LeftUppercutLoMake":1,  "_id":0}).distinct('LeftUppercutLoMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"LeftUppercutLoMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"LegKicksAbsorbed":1,  "_id":0}).distinct('LegKicksAbsorbed');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"LegKicksAbsorbed": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"LeglockAttempt":1,  "_id":0}).distinct('LeglockAttempt');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"LeglockAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"LossesVsOrthodox":1,  "_id":0}).distinct('LossesVsOrthodox');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"LossesVsOrthodox": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"LossesVsSouthpaw":1,  "_id":0}).distinct('LossesVsSouthpaw');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"LossesVsSouthpaw": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"LossesVsSwitch":1,  "_id":0}).distinct('LossesVsSwitch');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"LossesVsSwitch": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"NeckCrankAttempt":1,  "_id":0}).distinct('NeckCrankAttempt');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"NeckCrankAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"OmoplataAttempt":1,  "_id":0}).distinct('OmoplataAttempt');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"OmoplataAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"OmoplataAttempts":1,  "_id":0}).distinct('OmoplataAttempts');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"OmoplataAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"OtherSubAttempt":1,  "_id":0}).distinct('OtherSubAttempt');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"OtherSubAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"OverhandsAbsorbed":1,  "_id":0}).distinct('OverhandsAbsorbed');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"OverhandsAbsorbed": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"RightBodyKickMake":1,  "_id":0}).distinct('RightBodyKickMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"RightBodyKickMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"RightElbowMake":1,  "_id":0}).distinct('RightElbowMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"RightElbowMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"RightHighKickMake":1,  "_id":0}).distinct('RightHighKickMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"RightHighKickMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"RightHookHiMake":1,  "_id":0}).distinct('RightHookHiMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"RightHookHiMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"RightHookLoMake":1,  "_id":0}).distinct('RightHookLoMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"RightHookLoMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"RightJabHiMake":1,  "_id":0}).distinct('RightJabHiMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"RightJabHiMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"RightJabLoMake":1,  "_id":0}).distinct('RightJabLoMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"RightJabLoMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"RightLegKickMake":1,  "_id":0}).distinct('RightLegKickMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"RightLegKickMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"RightOverhandMake":1,  "_id":0}).distinct('RightOverhandMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"RightOverhandMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"RightSpinBackFistMake":1,  "_id":0}).distinct('RightSpinBackFistMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"RightSpinBackFistMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"RightStraightHiMake":1,  "_id":0}).distinct('RightStraightHiMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"RightStraightHiMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"RightStraightLoMake":1,  "_id":0}).distinct('RightStraightLoMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"RightStraightLoMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"RightUppercutHiMake":1,  "_id":0}).distinct('RightUppercutHiMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"RightUppercutHiMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"RightUppercutLoMake":1,  "_id":0}).distinct('RightUppercutLoMake');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"RightUppercutLoMake": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"SUBRNCAttempt":1,  "_id":0}).distinct('SUBRNCAttempt');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"SUBRNCAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"SingleLegTakedownAttempts":1,  "_id":0}).distinct('SingleLegTakedownAttempts');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"SingleLegTakedownAttempts": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"StraightsAbsorbed":1,  "_id":0}).distinct('StraightsAbsorbed');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"StraightsAbsorbed": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"SubArmTriangleAttempt":1,  "_id":0}).distinct('SubArmTriangleAttempt');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"SubArmTriangleAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"SubAttempts":1,  "_id":0}).distinct('SubAttempts');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"SubAttempts": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"SubDarceAttempt":1,  "_id":0}).distinct('SubDarceAttempt');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"SubDarceAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"SubGuillotineAttempt":1,  "_id":0}).distinct('SubGuillotineAttempt');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"SubGuillotineAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"SubHeelHookAttempt":1,  "_id":0}).distinct('SubHeelHookAttempt');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"SubHeelHookAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"SubKimuraAttempt":1,  "_id":0}).distinct('SubKimuraAttempt');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"SubKimuraAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"SubNeckCrankAttempt":1,  "_id":0}).distinct('SubNeckCrankAttempt');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"SubNeckCrankAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"SubStraightArmLockAttempt":1,  "_id":0}).distinct('SubStraightArmLockAttempt');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"SubStraightArmLockAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"SubSulovStretchAttempt":1,  "_id":0}).distinct('SubSulovStretchAttempt');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"SubSulovStretchAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"SubTriangleArmbarAttempt":1,  "_id":0}).distinct('SubTriangleArmbarAttempt');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"SubTriangleArmbarAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"SubTriangleAttempt":1,  "_id":0}).distinct('SubTriangleAttempt');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"SubTriangleAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalBodyKicksMade":1,  "_id":0}).distinct('TotalBodyKicksMade');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalBodyKicksMade": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalBodyKicksThrown":1,  "_id":0}).distinct('TotalBodyKicksThrown');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalBodyKicksThrown": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalClinchStrikesMade":1,  "_id":0}).distinct('TotalClinchStrikesMade');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalClinchStrikesMade": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalClinchStrikesThrown":1,  "_id":0}).distinct('TotalClinchStrikesThrown');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalClinchStrikesThrown": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalElbowsMade":1,  "_id":0}).distinct('TotalElbowsMade');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalElbowsMade": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalElbowsThrown":1,  "_id":0}).distinct('TotalElbowsThrown');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalElbowsThrown": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalGroundStrikesMade":1,  "_id":0}).distinct('TotalGroundStrikesMade');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalGroundStrikesMade": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalGroundStrikesThrown":1,  "_id":0}).distinct('TotalGroundStrikesThrown');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalGroundStrikesThrown": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalHighKicksMade":1,  "_id":0}).distinct('TotalHighKicksMade');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalHighKicksMade": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalHighKicksThrown":1,  "_id":0}).distinct('TotalHighKicksThrown');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalHighKicksThrown": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalHooksMade":1,  "_id":0}).distinct('TotalHooksMade');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalHooksMade": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalHooksThrown":1,  "_id":0}).distinct('TotalHooksThrown');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalHooksThrown": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalJabsMade":1,  "_id":0}).distinct('TotalJabsMade');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalJabsMade": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalJabsThrown":1,  "_id":0}).distinct('TotalJabsThrown');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalJabsThrown": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalKicksLanded":1,  "_id":0}).distinct('TotalKicksLanded');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalKicksLanded": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalKicksThrown":1,  "_id":0}).distinct('TotalKicksThrown');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalKicksThrown": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalLegKicksMade":1,  "_id":0}).distinct('TotalLegKicksMade');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalLegKicksMade": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalLegKicksThrown":1,  "_id":0}).distinct('TotalLegKicksThrown');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalLegKicksThrown": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalOverhandsMade":1,  "_id":0}).distinct('TotalOverhandsMade');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalOverhandsMade": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalOverhandsThrown":1,  "_id":0}).distinct('TotalOverhandsThrown');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalOverhandsThrown": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalPunchesLanded":1,  "_id":0}).distinct('TotalPunchesLanded');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalPunchesLanded": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalPunchesThrown":1,  "_id":0}).distinct('TotalPunchesThrown');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalPunchesThrown": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalSpinBackFistsMade":1,  "_id":0}).distinct('TotalSpinBackFistsMade');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalSpinBackFistsMade": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalSpinBackFistsThrown":1,  "_id":0}).distinct('TotalSpinBackFistsThrown');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalSpinBackFistsThrown": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalStraightsMade":1,  "_id":0}).distinct('TotalStraightsMade');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalStraightsMade": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalStraightsThrown":1,  "_id":0}).distinct('TotalStraightsThrown');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalStraightsThrown": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalStrikesLanded":1,  "_id":0}).distinct('TotalStrikesLanded');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalStrikesLanded": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalUppercutsMade":1,  "_id":0}).distinct('TotalUppercutsMade');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalUppercutsMade": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TotalUppercutsThrown":1,  "_id":0}).distinct('TotalUppercutsThrown');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TotalUppercutsThrown": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TripTakedownAttempts":1,  "_id":0}).distinct('TripTakedownAttempts');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TripTakedownAttempts": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"TwisterAttempts":1,  "_id":0}).distinct('TwisterAttempts');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"TwisterAttempts": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"UppercutsAbsorbed":1,  "_id":0}).distinct('UppercutsAbsorbed');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"UppercutsAbsorbed": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"VonFlueAttempt":1,  "_id":0}).distinct('VonFlueAttempt');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"VonFlueAttempt": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"WinsVsOrthodox":1,  "_id":0}).distinct('WinsVsOrthodox');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"WinsVsOrthodox": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"WinsVsSouthpaw":1,  "_id":0}).distinct('WinsVsSouthpaw');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"WinsVsSouthpaw": l[0]}})
        l = db.FighterData.find({"fighterCode":y},{"WinsVsSwitch":1,  "_id":0}).distinct('WinsVsSwitch');
        db.WCAV.update_one({"weight":weightnum}, {"$inc": {"WinsVsSwitch": l[0]}})
print("Done")


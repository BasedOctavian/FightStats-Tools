import pymongo


myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@cluster0.hufkz1t.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]
fighterdata = db["FighterData"]
fightername = db["FighterNames"]
wcav = db["WCAV"]

weight = int()

firstname = int()
firstname = input("Enter First Name: ")
firstname.upper()
firstname.strip()
lastname = int()
lastname = input("Enter Last Name: ")
lastname.upper()
lastname.strip()
nickname = int()
nickname = input("Enter Nickname: ")
nickname.title()
mlpredstr = input("Enter ML Predictor Num: ")
mlpred = float(mlpredstr)
fightercode = firstname + lastname + nickname
print(fightercode)


#Gets The Weight For The Entered Fighter From The FighterDB
l = db.FighterNames.find({"fighterCode":fightercode},{"weight":1,  "_id":0}).distinct('weight'); weight = l[0]




#Gets The Minutes For The Fighter
l = db.FighterData.find({"fighterCode":fightercode},{"MinutesTracked":1,  "_id":0}).distinct('MinutesTracked'); fmin = l[0]
#Gets The Minutes For The WC
l = db.WCAV.find({"weight":weight},{"minutes":1,  "_id":0}).distinct('minutes'); wmin = l[0]
#Gets The Rounds For The Fighter
l = db.FighterData.find({"fighterCode":fightercode},{"RoundsTracked":1,  "_id":0}).distinct('RoundsTracked'); fround = l[0]
#Gets The Rounds For The WC
l = db.WCAV.find({"weight":weight},{"rounds":1,  "_id":0}).distinct('rounds'); wround = l[0]
#Gets The Fights For The Fighter
l = db.FighterData.find({"fighterCode":fightercode},{"FightsTracked":1,  "_id":0}).distinct('FightsTracked'); ffights = l[0]
#Gets The Fights For The WC
l = db.WCAV.find({"weight":weight},{"fights":1,  "_id":0}).distinct('fights'); wfights = l[0]

#Gets The Ko Wins Per Fight For The Fighter
l = db.FighterData.find({"fighterCode":fightercode},{"FighterKOWins":1,  "_id":0}).distinct('FighterKOWins');
fkowins = (l[0]) / (ffights)
#Gets The Ko Wins Per Fight For The WC
l = db.WCAV.find({"weight":weight},{"kowins":1,  "_id":0}).distinct('kowins'); wkowins = (l[0]) / (wfights)

#Gets The TKo Wins Per Fight For The Fighter
l = db.FighterData.find({"fighterCode":fightercode},{"FighterTKOWins":1,  "_id":0}).distinct('FighterTKOWins');
ftkowins = (l[0]) / (ffights)
#Gets The TKo Wins Per Fight For The WC
l = db.WCAV.find({"weight":weight},{"tkowins":1,  "_id":0}).distinct('tkowins'); wtkowins = (l[0]) / (wfights)

#Gets The Num of Knockdowns Per Minute For The Fighter
l = db.FighterData.find({"fighterCode":fightercode},{"NumberOfKnockDowns":1,  "_id":0}).distinct('NumberOfKnockDowns');
fnumofknockdowns = (l[0]) / (fmin)

#Gets The Num of Knockdowns Per Minute For The WC
l = db.WCAV.find({"weight":weight},{"numberofknockdowns":1,  "_id":0}).distinct('numberofknockdowns'); 
wnumofknockdowns = (l[0]) / (wmin)




#Gets The Num of Stuns Per Minute For The Fighter
l = db.FighterData.find({"fighterCode":fightercode},{"NumberOfStuns":1,  "_id":0}).distinct('NumberOfStuns');
fnumofstuns = (l[0]) / (fmin)

#Gets The Num of Stuns Per Minute For The WC
l = db.WCAV.find({"weight":weight},{"numberofstuns":1,  "_id":0}).distinct('numberofstuns'); 
wnumofstuns = (l[0]) / (wmin)



#Gets The Num of Hooks Landed Per Minute For The Fighter
l = db.FighterData.find({"fighterCode":fightercode},{"TotalHooksMade":1,  "_id":0}).distinct('TotalHooksMade');
fhooksmade = (l[0]) / (fmin)
#Gets The Num of Hooks Landed Per Minute For The WC
l = db.WCAV.find({"weight":weight},{"TotalHooksMade":1,  "_id":0}).distinct("TotalHooksMade"); 
whooksmade = (l[0]) / (wmin)

#Gets The Num of Straights Landed Per Minute For The Fighter
l = db.FighterData.find({"fighterCode":fightercode},{"TotalStraightsMade":1,  "_id":0}).distinct('TotalStraightsMade');
fstraightsmade = (l[0]) / (fmin)
#Gets The Num of Straights Landed Per Minute For The WC
l = db.WCAV.find({"weight":weight},{"TotalStraightsMade":1,  "_id":0}).distinct("TotalStraightsMade"); 
wstraightsmade = (l[0]) / (wmin)

#Gets The Num of Overhands Landed Per Minute For The Fighter
l = db.FighterData.find({"fighterCode":fightercode},{"TotalOverhandsMade":1,  "_id":0}).distinct('TotalOverhandsMade');
foverhandsmade = (l[0]) / (fmin)
#Gets The Num of Overhands Landed Per Minute For The WC
l = db.WCAV.find({"weight":weight},{"TotalOverhandsMade":1,  "_id":0}).distinct("TotalOverhandsMade"); 
woverhandsmade = (l[0]) / (wmin)

#Gets The Num of Uppercuts Landed Per Minute For The Fighter
l = db.FighterData.find({"fighterCode":fightercode},{"TotalUppercutsMade":1,  "_id":0}).distinct('TotalUppercutsMade');
fuppercutsmade = (l[0]) / (fmin)
#Gets The Num of Uppercuts Landed Per Minute For The WC
l = db.WCAV.find({"weight":weight},{"TotalUppercutsMade":1,  "_id":0}).distinct("TotalUppercutsMade"); 
wuppercutsmade = (l[0]) / (wmin)



output = (
    ((((fkowins - wkowins) * 320) + ((ftkowins - wtkowins) * 390))) +
    ((fnumofknockdowns - wnumofknockdowns) * 1810) +
    ((fnumofstuns - wnumofstuns) * 480) -
    ((fhooksmade - whooksmade) * 110) -
    ((fstraightsmade - wstraightsmade) * 110) -
    ((foverhandsmade - woverhandsmade) * 120) -
    ((fuppercutsmade - wuppercutsmade) * 114) 
    )

output = output / 5
output = output + 62
output = (output / 3) + 60

if weight == 125:
    output = output + 8
if weight == 135:
    output = output + 5
if weight == 145:
    output = output + 3
if weight == 155:
    output = output + 2
if weight == 170:
    output = output  + 2
if weight == 185:
    output = output + 1
if weight == 205:
    output = output - 2
if weight == 265:
    output = output - 4

output = output - 3



if output < 65:
    output = 65
if output > 99:
    output = output - 9
if output >= 99:
    output = 99

powerGrade = round(output, 1)

powerchanged = False

if powerGrade >= 99:
    powerGrade = powerGrade - 6
    powerchanged = True

if powerchanged == True:
    if powerGrade < 95:
        powerGrade = powerGrade + 3


if fmin < 4 or ffights < 2:
    print("Not Enough Data For Power Grade")
    output = 0







#Gets The Num of Takedowns Landed & Attempted For A Fighter
l = db.FighterData.find({"fighterCode":fightercode},{"SingleLegTakedownSuccess":1,  "_id":0}).distinct('SingleLegTakedownSuccess');
fsinglelegsuccess = (l[0]) / (fmin)
l = db.FighterData.find({"fighterCode":fightercode},{"SingleLegTakedownAttempts":1,  "_id":0}).distinct('SingleLegTakedownAttempts');
fsinglelegattempt = (l[0]) / (fmin)

l = db.FighterData.find({"fighterCode":fightercode},{"DoubleLegTakedownSuccess":1,  "_id":0}).distinct('DoubleLegTakedownSuccess');
fdoublelegsuccess = (l[0]) / (fmin)
l = db.FighterData.find({"fighterCode":fightercode},{"DoubleLegTakedownAttempts":1,  "_id":0}).distinct('DoubleLegTakedownAttempts');
fdoublelegattempt = (l[0]) / (fmin)

l = db.FighterData.find({"fighterCode":fightercode},{"TripTakedownSuccess":1,  "_id":0}).distinct('TripTakedownSuccess');
ftripsuccess = (l[0]) / (fmin)
l = db.FighterData.find({"fighterCode":fightercode},{"TripTakedownAttempts":1,  "_id":0}).distinct('TripTakedownAttempts');
ftripattempt = (l[0]) / (fmin)

l = db.FighterData.find({"fighterCode":fightercode},{"BodyLockTakedownSuccess":1,  "_id":0}).distinct('BodyLockTakedownSuccess');
fbodylocksuccess = (l[0]) / (fmin)
l = db.FighterData.find({"fighterCode":fightercode},{"BodyLockTakedownAttempts":1,  "_id":0}).distinct('BodyLockTakedownAttempts');
fbodylockattempt = (l[0]) / (fmin)

l = db.FighterData.find({"fighterCode":fightercode},{"SuccessfulThrowTD":1,  "_id":0}).distinct('SuccessfulThrowTD');
fthrowsuccess = (l[0]) / (fmin)
l = db.FighterData.find({"fighterCode":fightercode},{"AttemptedThrowTD":1,  "_id":0}).distinct('AttemptedThrowTD');
fthrowattempt = (l[0]) / (fmin)



output = (
    
         ((fthrowsuccess * 1.6 + 0.1) / (fthrowattempt * 0.2 + 0.1)) +
         ((fbodylocksuccess * 1.6 + 0.1) / (fbodylockattempt * 0.2 + 0.1)) +
         ((ftripsuccess * 1.6 + 0.1) / (ftripattempt * 0.2 + 0.1)) +
         ((fdoublelegsuccess * 1.6 + 0.1) / (fdoublelegattempt * 0.2 + 0.1)) +
         ((fsinglelegsuccess * 1.6 + 0.1) / (fsinglelegattempt * 0.2 + 0.1)) 
    )


output = 70 + output



if weight == 125:
    output = output + 10
if weight == 135:
    output = output + 10
if weight == 145:
    output = output + 10
if weight == 155:
    output = output + 11
if weight == 170:
    output = output  + 11
if weight == 185:
    output = output + 12
if weight == 205:
    output = output + 13
if weight == 265:
    output = output + 16



total = int()
 
l = db.FighterData.find({"fighterCode":fightercode},{"AttemptedThrowTD":1,  "_id":0}).distinct('AttemptedThrowTD');
total = l[0]

l = db.FighterData.find({"fighterCode":fightercode},{"BodyLockTakedownAttempts":1,  "_id":0}).distinct('BodyLockTakedownAttempts');
total = total + l[0]
l = db.FighterData.find({"fighterCode":fightercode},{"TripTakedownAttempts":1,  "_id":0}).distinct('TripTakedownAttempts');
total = total + l[0]
l = db.FighterData.find({"fighterCode":fightercode},{"DoubleLegTakedownAttempts":1,  "_id":0}).distinct('DoubleLegTakedownAttempts');
total = total + l[0]
l = db.FighterData.find({"fighterCode":fightercode},{"SingleLegTakedownAttempts":1,  "_id":0}).distinct('SingleLegTakedownAttempts');
total = total + l[0]


if output < 65:
    output = 65
if output > 99:
    output = output - 9
if output >= 99:
    output = 99


if  total > 5:
    output = output
else:
    output = 0

tdGrade = round(output, 1)


  
tdgrade2 = tdGrade
  


def getFighterStatByMin(statCode):
    l = db.FighterData.find({"fighterCode":fightercode},{statCode:1,  "_id":0}).distinct(statCode);
    fighteroutput = (l[0]) / (fmin)
    
def getWCAVStatByMin(statCode):
    l = db.WCAV.find({"weight":weight},{statCode:1,  "_id":0}).distinct(statCode); 
    wcavoutput = (l[0]) / (wmin)
    
 



l = db.FighterData.find({"fighterCode":fightercode},{"TotalStraightsThrown":1,  "_id":0}).distinct('TotalStraightsThrown');
fstraightsthrown = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"TotalStraightsThrown":1,  "_id":0}).distinct('TotalStraightsThrown'); 
wcavstraightsthrown = (l[0]) / (wmin)

l = db.FighterData.find({"fighterCode":fightercode},{"TotalHooksThrown":1,  "_id":0}).distinct('TotalHooksThrown');
fhooksthrown = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"TotalHooksThrown":1,  "_id":0}).distinct('TotalHooksThrown'); 
whooksthrown = (l[0]) / (wmin)

l = db.FighterData.find({"fighterCode":fightercode},{"TotalOverhandsThrown":1,  "_id":0}).distinct('TotalOverhandsThrown');
foverhandsthrown = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"TotalOverhandsThrown":1,  "_id":0}).distinct('TotalOverhandsThrown'); 
woverhandsthrown = (l[0]) / (wmin)

l = db.FighterData.find({"fighterCode":fightercode},{"TotalUppercutsThrown":1,  "_id":0}).distinct('TotalUppercutsThrown');
fuppercutsthrown = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"TotalUppercutsThrown":1,  "_id":0}).distinct('TotalUppercutsThrown'); 
wuppercutsthrown = (l[0]) / (wmin)

l = db.FighterData.find({"fighterCode":fightercode},{"TotalLegKicksThrown":1,  "_id":0}).distinct('TotalLegKicksThrown');
flegkicksthrown = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"TotalLegKicksThrown":1,  "_id":0}).distinct('TotalLegKicksThrown'); 
wlegkicksthrown = (l[0]) / (wmin)

l = db.FighterData.find({"fighterCode":fightercode},{"TotalLegKicksMade":1,  "_id":0}).distinct('TotalLegKicksMade');
flegkicksmade = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"TotalLegKicksMade":1,  "_id":0}).distinct('TotalLegKicksMade'); 
wlegkicksmade = (l[0]) / (wmin)

l = db.FighterData.find({"fighterCode":fightercode},{"TotalBodyKicksThrown":1,  "_id":0}).distinct('TotalBodyKicksThrown');
fbodykicksthrown = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"TotalBodyKicksThrown":1,  "_id":0}).distinct('TotalBodyKicksThrown'); 
wbodykicksthrown = (l[0]) / (wmin)

l = db.FighterData.find({"fighterCode":fightercode},{"TotalBodyKicksMade":1,  "_id":0}).distinct('TotalBodyKicksMade');
fbodykicksmade = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"TotalBodyKicksMade":1,  "_id":0}).distinct('TotalBodyKicksMade'); 
wbodykicksmade = (l[0]) / (wmin)

l = db.FighterData.find({"fighterCode":fightercode},{"TotalHighKicksThrown":1,  "_id":0}).distinct('TotalHighKicksThrown');
fhighkicksthrown = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"TotalHighKicksThrown":1,  "_id":0}).distinct('TotalHighKicksThrown'); 
whighkicksthrown = (l[0]) / (wmin)

l = db.FighterData.find({"fighterCode":fightercode},{"TotalHighKicksMade":1,  "_id":0}).distinct('TotalHighKicksMade');
fhighkicksmade = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"TotalHighKicksMade":1,  "_id":0}).distinct('TotalHighKicksMade'); 
whighkicksmade = (l[0]) / (wmin)

l = db.FighterData.find({"fighterCode":fightercode},{"TotalJabsThrown":1,  "_id":0}).distinct('TotalJabsThrown');
fjabsthrown = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"TotalJabsThrown":1,  "_id":0}).distinct('TotalJabsThrown'); 
wjabsthrown = (l[0]) / (wmin)

l = db.FighterData.find({"fighterCode":fightercode},{"TotalJabsMade":1,  "_id":0}).distinct('TotalJabsMade');
fjabsmade = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"TotalJabsMade":1,  "_id":0}).distinct('TotalJabsMade'); 
wjabsmade = (l[0]) / (wmin)

l = db.FighterData.find({"fighterCode":fightercode},{"JabsAbsorbed":1,  "_id":0}).distinct('JabsAbsorbed');
fjabsabsorbed = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"JabsAbsorbed":1,  "_id":0}).distinct('JabsAbsorbed'); 
wjabsabsorbed = (l[0]) / (wmin)

l = db.FighterData.find({"fighterCode":fightercode},{"StraightsAbsorbed":1,  "_id":0}).distinct('StraightsAbsorbed');
fstraightsabsorbed = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"StraightsAbsorbed":1,  "_id":0}).distinct('StraightsAbsorbed'); 
wstraightsabsorbed = (l[0]) / (wmin)

l = db.FighterData.find({"fighterCode":fightercode},{"HooksAbsorbed":1,  "_id":0}).distinct('HooksAbsorbed');
fhooksabsorbed = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"HooksAbsorbed":1,  "_id":0}).distinct('HooksAbsorbed'); 
whooksabsorbed = (l[0]) / (wmin)

l = db.FighterData.find({"fighterCode":fightercode},{"UppercutsAbsorbed":1,  "_id":0}).distinct('UppercutsAbsorbed');
fuppercutsabsorbed = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"UppercutsAbsorbed":1,  "_id":0}).distinct('UppercutsAbsorbed'); 
wuppercutsabsorbed = (l[0]) / (wmin)

l = db.FighterData.find({"fighterCode":fightercode},{"LegKicksAbsorbed":1,  "_id":0}).distinct('LegKicksAbsorbed');
flegkicksabsorbed = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"LegKicksAbsorbed":1,  "_id":0}).distinct('LegKicksAbsorbed'); 
wlegkicksabsorbed = (l[0]) / (wmin)

l = db.FighterData.find({"fighterCode":fightercode},{"HeadKicksAbsorbed":1,  "_id":0}).distinct('HeadKicksAbsorbed');
fheadkicksabsorbed = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"HeadKicksAbsorbed":1,  "_id":0}).distinct('HeadKicksAbsorbed'); 
wheadkicksabsorbed = (l[0]) / (wmin)

l = db.FighterData.find({"fighterCode":fightercode},{"BodyKicksAbsorbed":1,  "_id":0}).distinct('BodyKicksAbsorbed');
fbodykicksabsorbed = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"BodyKicksAbsorbed":1,  "_id":0}).distinct('BodyKicksAbsorbed'); 
wbodykicksabsorbed = (l[0]) / (wmin)

total = 0

l = db.FighterData.find({"fighterCode":fightercode},{"TimesSingleLegged":1,  "_id":0}).distinct('TimesSingleLegged');
ftimesinglelegged = (l[0]) / (fmin)
total = total + l[0]

l = db.FighterData.find({"fighterCode":fightercode},{"TimesDoubleLegged":1,  "_id":0}).distinct('TimesDoubleLegged');
ftimesdoublelegged = (l[0]) / (fmin)
total = total + l[0]

l = db.FighterData.find({"fighterCode":fightercode},{"TimesTripped":1,  "_id":0}).distinct('TimesTripped');
ftimestripped = (l[0]) / (fmin)
total = total + l[0]

l = db.FighterData.find({"fighterCode":fightercode},{"TimesBodyLocked":1,  "_id":0}).distinct('TimesBodyLocked');
ftimesbodylocked = (l[0]) / (fmin)
total = total + l[0]

l = db.FighterData.find({"fighterCode":fightercode},{"SingleLegDefends":1,  "_id":0}).distinct('SingleLegDefends');
fsinglelegdefends = (l[0]) / (fmin)
total = total + l[0]

l = db.FighterData.find({"fighterCode":fightercode},{"DoubleLegDefends":1,  "_id":0}).distinct('DoubleLegDefends');
fdoublelegdefends = (l[0]) / (fmin)
total = total + l[0]

l = db.FighterData.find({"fighterCode":fightercode},{"TripDefends":1,  "_id":0}).distinct('TripDefends');
ftripdefends = (l[0]) / (fmin)
total = total + l[0]

l = db.FighterData.find({"fighterCode":fightercode},{"BodyLockDefends":1,  "_id":0}).distinct('BodyLockDefends');
fbodylockdefends = (l[0]) / (fmin)
total = total + l[0]

l = db.FighterData.find({"fighterCode":fightercode},{"TimesThrown":1,  "_id":0}).distinct('TimesThrown');
ftimesthrown = (l[0]) / (fmin)

l = db.FighterData.find({"fighterCode":fightercode},{"ThrowDefends":1,  "_id":0}).distinct('ThrowDefends');
fthrowdefends = (l[0]) / (fmin)
total = total + l[0]

l = db.FighterData.find({"fighterCode":fightercode},{"TimesKnockedDown":1,  "_id":0}).distinct('TimesKnockedDown');
ftimesknockeddown = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"timesknockeddown":1,  "_id":0}).distinct('timesknockeddown'); 
wtimesknockeddown = (l[0]) / (wmin)

l = db.FighterData.find({"fighterCode":fightercode},{"TimesStunned":1,  "_id":0}).distinct('TimesStunned');
ftimesstunned = (l[0]) / (fmin)

l = db.WCAV.find({"weight":weight},{"timesstunned":1,  "_id":0}).distinct('timesstunned'); 
wtimesstunned = (l[0]) / (wmin)

l = db.FighterData.find({"fighterCode":fightercode},{"WinsInTitleFights":1,  "_id":0}).distinct('WinsInTitleFights');
fwinsintitlefights = (l[0]) 

l = db.FighterData.find({"fighterCode":fightercode},{"LossesInTitleFights":1,  "_id":0}).distinct('LossesInTitleFights');
flossesintitlefights = (l[0]) 

l = db.FighterData.find({"fighterCode":fightercode},{"Round5StrikesLanded":1,  "_id":0}).distinct('Round5StrikesLanded');
fround5strikes = (l[0]) 





#TD Defense Grade

output = (
    
         ((fthrowdefends * 1.9 + 0.1) - (ftimesthrown * 3 + 0.1)) +
         ((fbodylockdefends * 1.9 + 0.1) / (ftimesbodylocked * 3 + 0.1)) +
         ((ftripdefends * 1.9 + 0.1) / (ftimestripped * 3 + 0.1)) +
         ((fdoublelegdefends * 2.2 + 0.1) / (ftimesdoublelegged * 3.2 + 0.1)) +
         ((fsinglelegdefends * 2.2 + 0.1) / (ftimesinglelegged * 3.2 + 0.1)) 
    )


output = output * 13.5


if weight == 125:
    output = output + 9
if weight == 135:
    output = output + 13
if weight == 145:
    output = output + 13
if weight == 155:
    output = output + 13
if weight == 170:
    output = output  + 12
if weight == 185:
    output = output + 10
if weight == 205:
    output = output + 9
if weight == 265:
    output = output + 6





 
l = db.FighterData.find({"fighterCode":fightercode},{"SingleLegDefends":1,  "_id":0}).distinct('SingleLegDefends');
total = l[0] 
l = db.FighterData.find({"fighterCode":fightercode},{"TimesSingleLegged":1,  "_id":0}).distinct('TimesSingleLegged');
total = l[0] + total

l = db.FighterData.find({"fighterCode":fightercode},{"TimesDoubleLegged":1,  "_id":0}).distinct('TimesDoubleLegged');
total = l[0] + total

l = db.FighterData.find({"fighterCode":fightercode},{"TimesBodyLocked":1,  "_id":0}).distinct('TimesBodyLocked');
total = l[0] + total


l = db.FighterData.find({"fighterCode":fightercode},{"DoubleLegDefends":1,  "_id":0}).distinct('DoubleLegDefends');
total = total + l[0] 
l = db.FighterData.find({"fighterCode":fightercode},{"BodyLockDefends":1,  "_id":0}).distinct('BodyLockDefends');
total = total + l[0]
l = db.FighterData.find({"fighterCode":fightercode},{"TripDefends":1,  "_id":0}).distinct('TripDefends');
total = total + l[0]




if output < 65:
    output = 65
if output > 99:
    output = output - 9
if output >= 99:
    output = 99


if total < 1:
    output = 0

tdDGrade = round(output, 1)

tdGrade = (tdDGrade + tdGrade) / 2

if tdGrade < 65:
    tdGrade = 65
if tdGrade > 99:
    tdGrade = tdGrade - 9
if tdGrade >= 99:
    tdGrade = 99

if tdGrade >= 99:
    tdGrade = tdGrade - 5

tdGrade = round(tdGrade, 1)

grapplingGrade = int()



grapplingGrade = ((tdGrade * 7.5 + tdgrade2 * 1) / 6.9)
grapplingGrade = (grapplingGrade / 3) + 55



if weight == 125:
    grapplingGrade = (grapplingGrade / 1.5) + 33
if weight == 135:
    grapplingGrade = (grapplingGrade / 1.5) + 34
if weight == 145:
    grapplingGrade = (grapplingGrade / 1.5) + 22
if weight == 155:
    grapplingGrade = (grapplingGrade / 1.5) + 35
if weight == 170:
    grapplingGrade = (grapplingGrade / 2) + 35
if weight == 185:
    grapplingGrade = (grapplingGrade / 2) + 30
if weight == 205:
    grapplingGrade = (grapplingGrade / 2) + 31
if weight == 265:
    grapplingGrade = (grapplingGrade / 2) + 10



if grapplingGrade < 65:
    grapplingGrade = grapplingGrade + 23





if grapplingGrade < 65:
    grapplingGrade = 65
if grapplingGrade > 99:
    grapplingGrade = grapplingGrade - 9
if grapplingGrade >= 99:
    grapplingGrade = 99

if grapplingGrade >= 99:
    grapplingGrade = grapplingGrade - 5




grapplingGrade = round(grapplingGrade, 1)




if output == 0:
    print("Not Enough Data")
    #print("TD Defense Grade: ", tdGrade)


  





#Get The Kicking Grade



output = (
    ((((fkowins - wkowins) * 0) + ((ftkowins - wtkowins) * 0))) +
    ((flegkicksthrown - flegkicksmade) + flegkicksmade/3 / (wlegkicksthrown - wlegkicksmade) * 8130) +
    ((fbodykicksthrown - fbodykicksmade) + fbodykicksmade/3 / (wbodykicksthrown - wbodykicksmade) * 5900) +
    ((fhighkicksthrown - fhighkicksmade) + fhighkicksmade/3 / (whighkicksthrown - whighkicksmade) * 10850) -
    ((flegkicksabsorbed - wlegkicksabsorbed) * 150) -
    ((fbodykicksabsorbed - wbodykicksabsorbed) * 200) -
    ((fheadkicksabsorbed - wheadkicksabsorbed) * 500) 
    )
    




output = output / 3.7
output = output / 100
output = output * 7
output = output + 40
output = output / 1.8
output = output - 8



output = output / 6

if weight == 125:
    output = (output / 1) + 61
if weight == 135: 
    output = (output / 1) + 61
if weight == 145:
    output = (output / 1) + 75
if weight == 155:
    output = (output / 1) + 61
if weight == 170:
    output = (output / 1) + 61
if weight == 185:
    output = (output / 1) + 61
if weight == 205:
    output = (output / 1) + 61
if weight == 265:
    output = (output / 1) + 38



wasdropped = False

if output > 99:
    tempy = output - 100
    tempy = tempy - 40

    output = output + tempy
    wasdropped = True



if output < 65:
    output = 65
if output > 99:
    output = output - 9
if output >= 99:
    output = 99


if  ffights > 3 or fmin > 4:
    output = output
else:
    output = 0

kickingGrade = round(output, 1)

if kickingGrade > 99:
    tempy = kickingGrade - 100
    tempy = tempy - 108

    kickingGrade = kickingGrade + tempy
    
if wasdropped == True:
    if kickingGrade < 94:
        kickingGrade = kickingGrade + 4


if kickingGrade > 99:
    kickingGrade = 99

if kickingGrade >= 99:
    kickingGrade = kickingGrade - 5

if output == 0:
    print("Not Enough Data")








   
#Get The Striking Grade



output = (
    ((((fkowins - wkowins) * 290) + ((ftkowins - wtkowins) * 190))) +
    ((fnumofknockdowns - wnumofknockdowns) * 100640) +
    ((fnumofstuns - wnumofstuns) * 93080) -
    ((ftimesstunned - wtimesstunned) * 20380) -
    (ftimesknockeddown * 227680) +
    ((fhooksthrown - fhooksmade) + (fhooksmade/3) / (whooksthrown - whooksmade) * 6930) +
    ((fjabsthrown - fjabsmade) + (fjabsmade/3) / (wjabsthrown - wjabsmade) * 5800) +
    ((fstraightsthrown - fstraightsmade) + fstraightsmade/3 / (wcavstraightsthrown - wstraightsmade) * 6830) +
    ((foverhandsthrown - foverhandsmade) + foverhandsmade/3 / (woverhandsthrown - woverhandsmade) * 6630) +
    ((fuppercutsthrown - fuppercutsmade) + fuppercutsmade/3 / (wuppercutsthrown - wuppercutsmade) * 6700) +
    ((flegkicksthrown - flegkicksmade) + flegkicksmade/3 / (wlegkicksthrown - wlegkicksmade) * 6930) +
    ((fbodykicksthrown - fbodykicksmade) + fbodykicksmade/3 / (wbodykicksthrown - wbodykicksmade) * 3900) +
    ((fhighkicksthrown - fhighkicksmade) + fhighkicksmade/3 / (whighkicksthrown - whighkicksmade) * 15850) -
    ((flegkicksabsorbed - wlegkicksabsorbed) * 505) -
    ((fbodykicksabsorbed - wbodykicksabsorbed) * 419) -
    ((fheadkicksabsorbed - wheadkicksabsorbed) * 1185) -
    ((fjabsabsorbed - wjabsabsorbed) * 240) -
    ((fstraightsabsorbed - wstraightsabsorbed) * 683) -
    ((fhooksabsorbed - whooksabsorbed) * 440 -
    ((fuppercutsabsorbed - wuppercutsabsorbed) * 770) 
    )
    
)



output = output / 4
output = output / 100
output = output + 70
output = output + 40
output = output / 1.8
output = output - 8

if fwinsintitlefights > 0:
    temp = fwinsintitlefights * 4.95
    output = output + temp
    
if flossesintitlefights > 0:
    temp = flossesintitlefights * 1.75
    output = output - temp
    
if fround5strikes > 5:
    output = output + 2




if weight == 125:
    output = output + 19
if weight == 135:
    output = output + 17
if weight == 145:
    output = output + 15
if weight == 155:
    output = output + 11
if weight == 170:
    output = output  + 9
if weight == 185:
    output = output + 7
if weight == 205:
    output = output + 5
if weight == 265:
    output = output - 12



wasdropped = False

if output > 99:
    output = output - 13
    wasdropped = True



if output < 65:
    output = 65
if output > 99:
    output = output - 9
if output >= 99:
    output = 99


if  ffights > 3 or fmin > 4:
    output = output
else:
    output = 0

strikingGrade = output
strikingGrade = (strikingGrade + (kickingGrade / 2.9) + strikingGrade + (strikingGrade / 4.3)) -2.5

strikingGrade = strikingGrade / 2

strikingGrade = round(strikingGrade, 1)




if strikingGrade > 99:
    strikingGrade = strikingGrade - 14
    
if wasdropped == True:
    if strikingGrade < 94:
        strikingGrade = strikingGrade + 3




if strikingGrade > 99:
    strikingGrade = 99

if strikingGrade >= 99:
    strikingGrade = strikingGrade - 5

if output == 0:
    print("Not Enough Data")

  
  
  
  
  
  
  
  
#Get The Boxing Grade



output = (
    ((((fkowins - wkowins) * 290) + ((ftkowins - wtkowins) * 190))) +
    ((fnumofknockdowns - wnumofknockdowns) * 100640) +
    ((fnumofstuns - wnumofstuns) * 93080) -
    ((ftimesstunned - wtimesstunned) * 20380) -
    (ftimesknockeddown * 227680) +
    ((fhooksthrown - fhooksmade) + (fhooksmade/3) / (whooksthrown - whooksmade) * 6930) +
    ((fjabsthrown - fjabsmade) + (fjabsmade/3) / (wjabsthrown - wjabsmade) * 5400) +
    ((fstraightsthrown - fstraightsmade) + fstraightsmade/3 / (wcavstraightsthrown - wstraightsmade) * 5830) +
    ((foverhandsthrown - foverhandsmade) + foverhandsmade/3 / (woverhandsthrown - woverhandsmade) * 6630) +
    ((fuppercutsthrown - fuppercutsmade) + fuppercutsmade/3 / (wuppercutsthrown - wuppercutsmade) * 6700) +
    ((fjabsabsorbed - wjabsabsorbed) * 240) -
    ((fstraightsabsorbed - wstraightsabsorbed) * 683) -
    ((fhooksabsorbed - whooksabsorbed) * 440 -
    ((fuppercutsabsorbed - wuppercutsabsorbed) * 770) 
    )
    
)



output = output / 2.8
output = output / 100
output = output + (powerGrade / 2) + (strikingGrade / 2)
output = output + 40
output = output / 1.8
output = output - 8

if fwinsintitlefights > 0:
    temp = fwinsintitlefights * 4.95
    output = output + temp
    
if flossesintitlefights > 0:
    temp = flossesintitlefights * 1.75
    output = output - temp
    
if fround5strikes > 5:
    output = output + 2




if weight == 125:
    output = output + 12
if weight == 135:
    output = output + 10
if weight == 145:
    output = output + 7
if weight == 155:
    output = output + 5
if weight == 170:
    output = output  + 3
if weight == 185:
    output = output + 2
if weight == 205:
    output = output - 4
if weight == 265:
    output = output -8



wasdropped = False

if output > 99:
    tempy = output - 100
    tempy = tempy - 40

    output = output + tempy
    wasdropped = True



if output < 65:
    output = 65
if output > 99:
    output = output - 9
if output >= 99:
    output = 99


if  ffights > 3 or fmin > 8:
    output = output
else:
    output = 0

boxingGrade = round(output, 1)

if boxingGrade > 99:
    tempy = boxingGrade - 100
    tempy = tempy - 108
  
    boxingGrade = boxingGrade + tempy
    
if wasdropped == True:
    if boxingGrade < 94:
        boxingGrade = boxingGrade + 4


if boxingGrade > 99:
    boxingGrade = 99

if boxingGrade >= 99:
    boxingGrade = boxingGrade - 5
    
    
    
    
    
    
#Get The Striking Grade



output = (
    ((((fkowins - wkowins) * 290) + ((ftkowins - wtkowins) * 190))) +
    ((fnumofknockdowns - wnumofknockdowns) * 100640) +
    ((fnumofstuns - wnumofstuns) * 93080) -
    ((ftimesstunned - wtimesstunned) * 20380) -
    (ftimesknockeddown * 227680) +
    ((fhooksthrown - fhooksmade) + (fhooksmade/3) / (whooksthrown - whooksmade) * 6930) +
    ((fjabsthrown - fjabsmade) + (fjabsmade/3) / (wjabsthrown - wjabsmade) * 5400) +
    ((fstraightsthrown - fstraightsmade) + fstraightsmade/3 / (wcavstraightsthrown - wstraightsmade) * 5830) +
    ((foverhandsthrown - foverhandsmade) + foverhandsmade/3 / (woverhandsthrown - woverhandsmade) * 6630) +
    ((fuppercutsthrown - fuppercutsmade) + fuppercutsmade/3 / (wuppercutsthrown - wuppercutsmade) * 6700) +
    ((flegkicksthrown - flegkicksmade) + flegkicksmade/3 / (wlegkicksthrown - wlegkicksmade) * 6930) +
    ((fbodykicksthrown - fbodykicksmade) + fbodykicksmade/3 / (wbodykicksthrown - wbodykicksmade) * 3900) +
    ((fhighkicksthrown - fhighkicksmade) + fhighkicksmade/3 / (whighkicksthrown - whighkicksmade) * 15850) -
    ((flegkicksabsorbed - wlegkicksabsorbed) * 505) -
    ((fbodykicksabsorbed - wbodykicksabsorbed) * 419) -
    ((fheadkicksabsorbed - wheadkicksabsorbed) * 1185) -
    ((fjabsabsorbed - wjabsabsorbed) * 240) -
    ((fstraightsabsorbed - wstraightsabsorbed) * 683) -
    ((fhooksabsorbed - whooksabsorbed) * 440 -
    ((fuppercutsabsorbed - wuppercutsabsorbed) * 770) 
    )
    
)



output = output / 5
output = output / 100
output = output + powerGrade
output = output + 40
output = output / 1.8
output = output - 8

if fwinsintitlefights > 0:
    temp = fwinsintitlefights * 4.95
    output = output + temp
    
if flossesintitlefights > 0:
    temp = flossesintitlefights * 1.75
    output = output - temp
    
if fround5strikes > 5:
    output = output + 2




if weight == 125:
    output = output + 12
if weight == 135:
    output = output + 10
if weight == 145:
    output = output + 7
if weight == 155:
    output = output + 8
if weight == 170:
    output = output  + 3
if weight == 185:
    output = output + 2
if weight == 205:
    output = output - 2
if weight == 265:
    output = output -40



wasdropped = False

if output > 99:
    output = output - 13
    wasdropped = True



if output < 65:
    output = 65
if output > 99:
    output = output - 9
if output >= 99:
    output = 99


if  ffights > 3 or fmin > 4:
    output = output
else:
    output = 0



strikingGrade = output / 3

strikingGrade = (strikingGrade + (kickingGrade / 2.9) + strikingGrade + (strikingGrade / 4.3)) -4.5

strikingGrade = round(strikingGrade, 1)




if strikingGrade > 99:
    strikingGrade = strikingGrade - 14
    
if wasdropped == True:
    if strikingGrade < 94:
        strikingGrade = strikingGrade + 3




if strikingGrade > 99:
    strikingGrade = 99

if strikingGrade >= 99:
    strikingGrade = strikingGrade - 5

if output == 0:
    print("Not Enough Data")

#else:
  #print("Striking Grade: ", strikingGrade)
  
  
  
  
  
  
  
  
#Get The Defensive Grade



output = (
    ((fjabsabsorbed - wjabsabsorbed) * 740) -
    ((fstraightsabsorbed - wstraightsabsorbed) * 2683) -
    ((fhooksabsorbed - whooksabsorbed) * 3440) -
    ((flegkicksabsorbed - wlegkicksabsorbed) * 1240) -
    ((fbodykicksabsorbed - wbodykicksabsorbed) * 1100) -
    ((fheadkicksabsorbed - wheadkicksabsorbed) * 2440) -
    ((fuppercutsabsorbed - wuppercutsabsorbed) * 970)
    
    
    )




output = output / 100
output = abs(output)
output = 99 - output 



if weight == 125:
    output = (output / 3 ) + 40 + 12
if weight == 135:
    output = (output / 3 ) + 40 + 11
if weight == 145:
    output = (output / 3 ) + 40 + 9
if weight == 155:
    output = (output / 3 ) + 40 + 15
if weight == 170:
    output = (output / 3 ) + 40 + 13
if weight == 185:
    output = (output / 3 ) + 40 + 13
if weight == 205:
    output = (output / 3 ) + 40 + 12
if weight == 265:
    output = (output / 3 ) + 40 + 7



wasdropped = False

if output > 99:
    tempy = output - 100
    tempy = tempy - 40

    output = output + tempy
    wasdropped = True

if output < 65:
    output = output + 9

if output < 65:
    output = 65
if output > 99:
    output = output - 9
if output >= 99:
    output = 99



if  ffights > 3 or fmin > 4:
    output = output
else:
    output = 0

defenseGrade = round(output, 1)

if defenseGrade > 99:
    tempy = defenseGrade - 100
    tempy = tempy - 108
  
    defenseGrade = defenseGrade + tempy
    
if wasdropped == True:
    if defenseGrade < 94:
        defenseGrade = defenseGrade + 4


defenseGrade = defenseGrade + 9

if defenseGrade >= 99:
    defenseGrade = defenseGrade - 5
    
if defenseGrade > 99:
    defenseGrade = 99



  
  
output = (
    ((fstraightsabsorbed - wstraightsabsorbed) * 1683) +
    ((fhooksabsorbed - whooksabsorbed) * 2440) +
    ((flegkicksabsorbed - wlegkicksabsorbed) * 840) +
    ((fbodykicksabsorbed - wbodykicksabsorbed) * 1100) +
    ((fheadkicksabsorbed - wheadkicksabsorbed) * 2440) +
    ((fuppercutsabsorbed - wuppercutsabsorbed) * 970)  - 
    (ftimesstunned - wtimesstunned) * 11850 -
    (ftimesknockeddown - wtimesknockeddown) * 28900
)  





output = output / 40
output = output + 75
  
if weight == 125:
    output = (output / 3) + 62
if weight == 135:
    output = (output / 3) + 68
if weight == 145:
    output = (output / 3) + 83
if weight == 155:
    output = (output / 3) + 90
if weight == 170:
    output = (output / 3) + 91
if weight == 185:
    output = (output / 3) + 90
if weight == 205:
    output = (output / 3) + 94
if weight == 265:
    output = (output / 3) + 45



wasdropped = False

if output > 99:
    tempy = output - 100
    tempy = tempy - 40

    output = output + tempy
    wasdropped = True

if output < 65:
    output = output + 9

if output < 65:
    output = 65
if output > 99:
    output = output - 9
if output >= 99:
    output = 99


if  ffights > 3 or fmin > 4:
    output = output
else:
    output = 0

chinGrade = round(output, 1)

if chinGrade > 99:
    tempy = chinGrade - 100
    tempy = tempy - 108
  
    chinGrade = chinGrade + tempy
    
if wasdropped == True:
    if chinGrade < 94:
        chinGrade = chinGrade + 4


if chinGrade >= 99:
    chinGrade = chinGrade - 5
    
if chinGrade > 99:
    chinGrade = 99


print("Power Grade: ", powerGrade)
strikingGrade = (((strikingGrade * 90) + kickingGrade * 10)) / 100
print("Striking Grade: ", round(strikingGrade, 1))
print("Kicking Grade: ", kickingGrade)

if grapplingGrade < 75:
    grapplingGrade = (grapplingGrade * .1) + grapplingGrade
    

print("Grappling Grade: ", round(grapplingGrade, 1))
print("Defensive Grade: ", defenseGrade)
print("Chin Grade: ", chinGrade)



if weight != 265:
        fighterGrade = ((strikingGrade * 4.9) +
        (grapplingGrade * 10.0) +
        (defenseGrade * 2.2) +
        (chinGrade * 2.9) +
        (powerGrade * 1.5))
        
if weight == 265:
    fighterGrade = ((strikingGrade * 7.9) +
    (grapplingGrade * 4.0) +
    (defenseGrade * 4.8) +
    (chinGrade * 2.9) +
    (powerGrade * 1.5))


predictorIndex = ((strikingGrade ) +
(grapplingGrade * 5.5) +
(defenseGrade ) +
(chinGrade  * 1.5) +
(fighterGrade ) +
(powerGrade * 1.5))

fighterGrade = fighterGrade / 19.9


if weight == 125:
    fighterGrade = fighterGrade - 8.3
    
if weight == 135:
    fighterGrade = fighterGrade - 5.8
    
if weight == 145:
    fighterGrade = fighterGrade - 3.8
    
if weight == 155:
    fighterGrade = fighterGrade - 1.8
    
if weight == 170:
    fighterGrade = fighterGrade - 1.8
    
if weight == 185:
    fighterGrade = fighterGrade  - 2
    
if weight == 205:
    fighterGrade = fighterGrade  - 2.2
    
if weight == 265:
    fighterGrade = fighterGrade  - 2.2

fighterGrade = fighterGrade - 3

if fwinsintitlefights > 1:
    fighterGrade = fighterGrade + 3

if fighterGrade > 99:
    fighterGrade = 99


age = int()
age = input("Enter Age: ")

momentum = int()
momentum = input("Enter momentum +- from 5: ")

age = float(age)
print(age)

predictorIndex = predictorIndex - (age * 4.5)

predictorIndex = predictorIndex + (momentum * 10)

#print("Fighter Grade: ", round(fighterGrade, 1))
print("Math Predictor #: ", round(predictorIndex, 1))


mlpred1 = float()
mlpred2 = float()
mlpred3 = float()
mlpred4 = float()
mlpred5 = float()
mlpred6 = float()
mlpred7 = float()
mlpred8 = float()
mlpred9 = float()
mlpred10 = float()
mlpred11 = float()
mlpred12 = float()
mlpred13 = float()
mlpred14 = float()
mlpred15 = float()








mlpred1 = mlpred * 5200
mlpred2 = mlpred * 5000
mlpred3 = mlpred * 8000
mlpred4 = mlpred * 10000
mlpred5 = mlpred * 13000
mlpred6 = mlpred * 19000
mlpred7 = mlpred * 3200
mlpred8 = mlpred * 2200
mlpred9 = mlpred * 1600
mlpred10 = mlpred * 1400
mlpred11 = mlpred * 1300
mlpred12 = mlpred * 1200
mlpred13 = mlpred * 1000
mlpred14 = mlpred * 9000
mlpred15 = mlpred * 7600




print("MLPredictor 1: ", round(mlpred1 + predictorIndex, 1))
print("MLPredictor 2: ", round(mlpred2 + predictorIndex, 1))
print("MLPredictor 3: ", round(mlpred3 + predictorIndex, 1))
print("MLPredictor 4: ", round(mlpred4 + predictorIndex, 1))
print("MLPredictor 5: ", round(mlpred5 + predictorIndex, 1))
print("MLPredictor 6: ", round(mlpred6 + predictorIndex, 1))
print("MLPredictor 7: ", round(mlpred7 + predictorIndex, 1))
print("MLPredictor 8: ", round(mlpred8 + predictorIndex, 1))
print("MLPredictor 9: ", round(mlpred9 + predictorIndex, 1))
print("MLPredictor 10: ", round(mlpred10 + predictorIndex, 1))
print("MLPredictor 11: ", round(mlpred11 + predictorIndex, 1))
print("MLPredictor 12: ", round(mlpred12 + predictorIndex, 1))
print("MLPredictor 13: ", round(mlpred13 + predictorIndex, 1))
print("MLPredictor 14: ", round(mlpred14 + predictorIndex, 1))
print("MLPredictor 15: ", round(mlpred15 + predictorIndex, 1))




input("Enter Any Key To Quit")
SystemExit
import pymongo


fightsTracked = int()
minutesTracked = int()



topStrikesAbsorbed = list()
topTakedownsLanded = list()
topTakedownsAbsorbed = list()
topStrikesThrown = list()


#Setting Up The Connections To The DB
myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@cluster0.hufkz1t.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]
fighterdata = db["FighterData"]


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
y = firstname + lastname + nickname
print(y)


print("//////////////////////////////////")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("//////////////////////////////////")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("//////////////////////////////////")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")


l = db.FighterData.find({"fighterCode":y},{"FightsTracked":1,  "_id":0}).distinct('FightsTracked')
fightsTracked = l[0]
l = db.FighterData.find({"fighterCode":y},{"MinutesTracked":1,  "_id":0}).distinct('MinutesTracked');
minutesTracked = l[0]



if fightsTracked < 2:
    input("Not Enough Data")
    SystemExit
    
if minutesTracked < 2:
    input("Not Enough Data")
    SystemExit



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

l = db.FighterData.find({"fighterCode":y},{"StraightsAbsorbed":1,  "_id":0}).distinct('StraightsAbsorbed');
StraightsAbsorbed = l[0]

l = db.FighterData.find({"fighterCode":y},{"JabsAbsorbed":1,  "_id":0}).distinct('JabsAbsorbed');
JabsAbsorbed = l[0]



print("Strikes Landed: ", "\n",
     "Left Jab Hi: ", (leftHiJab / minutesTracked) * 5, "\n",
     "Left Jab Lo: ", (leftLoJab / minutesTracked) * 5, "\n",
     "Right Jab Hi: ", (RightHiJab / minutesTracked) * 5, "\n",
     "Right Jab Lo: ", (RightLoJab / minutesTracked) * 5, "\n",
     "Left Straight Hi: ", (leftHiStraight / minutesTracked) * 5, "\n",
     "Left Straight Lo: ", (leftLoStraight / minutesTracked) * 5, "\n",
     "Right Straight Hi: ", (RightHiStraight / minutesTracked) * 5, "\n",
     "Right Straight Lo: ", (RightLoStraight / minutesTracked) * 5, "\n",
     "Left Hook Hi: ", (leftHiHook / minutesTracked) * 5, "\n",
     "Left Hook Lo: ", (leftLoHook / minutesTracked) * 5, "\n",
     "Right Hook Hi: ", (RightHiHook / minutesTracked) * 5, "\n",
     "Right Hook Lo: ", (RightLoHook / minutesTracked) * 5, "\n",
     "Left Uppercut Hi: ", (leftHiUppercut / minutesTracked) * 5, "\n",
     "Left Uppercut Lo: ", (leftLoUppercut / minutesTracked) * 5, "\n",
     "Right Uppercut Hi: ", (RightHiUppercut / minutesTracked) * 5, "\n",
     "Right Uppercut Lo: ", (RightLoUppercut / minutesTracked) * 5, "\n",
     "Right Overhand: ", (rightOverhandMake / minutesTracked) * 5, "\n",
     "Left Overhand: ", (leftOverhandMake / minutesTracked) * 5, "\n",
     "Right Head Kick: ", (RightHighKick / minutesTracked) * 5, "\n",
     "Left Head Kick: ", (leftHighKick / minutesTracked) * 5, "\n",
     "Right Body Kick: ", (RightBodyKick / minutesTracked) * 5, "\n",
     "Left Body Kick: ", (leftBodyKick / minutesTracked) * 5, "\n",
     "Right Leg Kick: ", (RightLegKick / minutesTracked) * 5, "\n",
     "Left Leg Kick: ", (leftLegKick / minutesTracked) * 5, "\n",
     " " 
      )




print("Strikes Absorbed: ", "\n",
     "Jabs Absorbed: ", (JabsAbsorbed / minutesTracked) * 5, "\n",
     "Hooks Absorbed: ", (HooksAbsorbed / minutesTracked) * 5, "\n",
     "Straights Absorbed: ", (StraightsAbsorbed / minutesTracked) * 5, "\n",
     "Uppercuts Absorbed: ", (UppercutsAbsorbed / minutesTracked) * 5, "\n",
     "Head Kicks Absorbed: ", (HeadKicksAbsorbed / minutesTracked) * 5, "\n",
     "Body Kicks Absorbed: ", (BodyKicksAbsorbed / minutesTracked) * 5, "\n",
     "Leg Kicks Absorbed: ", (LegKicksAbsorbed / minutesTracked) * 5, "\n",
     " " 
      )


print("Takedowns Attempted: ", "\n",
     "Single Legs: ", singleLegTakedownAttempts / minutesTracked, "\n",
     "Double Legs: ", doubleLegTakedownAttempts / minutesTracked, "\n",
     "Bodylocks: ", bodyLockTakedownAttempts / minutesTracked, "\n",
     "Trips: ", tripTakedownAttempts / minutesTracked, "\n",
     "Throws: ", throwTakedownAttempts / minutesTracked, "\n",
     " "  
      )


print("Takedowns Absorbed: ", "\n",
     "Single Legs: ", timesSingleLegged / minutesTracked, "\n",
     "Double Legs: ", timesDoubleLegged / minutesTracked, "\n",
     "Bodylocks: ", timesBodyLocked / minutesTracked, "\n",
     "Trips: ", timesTripped / minutesTracked, "\n",
     "Throws: ", TimesThrown / minutesTracked, "\n",
     " "  
      )



input("Press Any Key To Exit")
SystemExit
import pymongo
import csv
import sqlite3
myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@octc1.d2he2mx.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]

webmatchupdata = db["WEBFighterMatchup"]

fighterA = "CurtisBlaydesRazor"
fighteraurl = fighterA.lower()
fighteraurl = fighteraurl.replace(' ', '-')
fighteraurl = 'https://www.fightstats.xyz/fighterdata/' + fighteraurl

fighterB = "SergeiPavlovich"
fighterburl = fighterB.lower()
fighterburl = fighterburl.replace(' ', '-')
fighterburl = 'https://www.fightstats.xyz/fighterdata/' + fighterburl

xox = db.WEBFighterData.find({"fighterCode":fighterA}, {"Image":1, "_id":0}).distinct('Image')
fighteraIMG = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterB}, {"Image":1, "_id":0}).distinct('Image')
fighterbIMG = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterA}, {"fighterName":1, "_id":0}).distinct('fighterName')
fighteraName = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterB}, {"fighterName":1, "_id":0}).distinct('fighterName')
fighterbName = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterA}, {"1Stance":1, "_id":0}).distinct('1Stance')
fighteraStance = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterB}, {"1Stance":1, "_id":0}).distinct('1Stance')
fighterbStance = xox[0]


xox = db.WEBFighterData.find({"fighterCode":fighterA}, {"1StrikeLanded":1, "_id":0}).distinct('1StrikeLanded')
a1strikelanded = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterA}, {"2StrikeLanded":1, "_id":0}).distinct('2StrikeLanded')
a2strikelanded = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterA}, {"3StrikeLanded":1, "_id":0}).distinct('3StrikeLanded')
a3strikelanded = xox[0]


xox = db.WEBFighterData.find({"fighterCode":fighterB}, {"1StrikeLanded":1, "_id":0}).distinct('1StrikeLanded')
b1strikelanded = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterB}, {"2StrikeLanded":1, "_id":0}).distinct('2StrikeLanded')
b2strikelanded = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterB}, {"3StrikeLanded":1, "_id":0}).distinct('3StrikeLanded')
b3strikelanded = xox[0]


xox = db.WEBFighterData.find({"fighterCode":fighterA}, {"height":1, "_id":0}).distinct('height')
aheight = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterB}, {"height":1, "_id":0}).distinct('height')
bheight = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterA}, {"FighterGrade":1, "_id":0}).distinct('FighterGrade')
afightergrade = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterA}, {"StrikingGrade":1, "_id":0}).distinct('StrikingGrade')
astrikinggrade = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterA}, {"GrapplingGrade":1, "_id":0}).distinct('GrapplingGrade')
agrapplinggrade = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterA}, {"DefensiveGrade":1, "_id":0}).distinct('DefensiveGrade')
adefensegrade = xox[0]


xox = db.WEBFighterData.find({"fighterCode":fighterB}, {"FighterGrade":1, "_id":0}).distinct('FighterGrade')
bfightergrade = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterB}, {"StrikingGrade":1, "_id":0}).distinct('StrikingGrade')
bstrikinggrade = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterB}, {"GrapplingGrade":1, "_id":0}).distinct('GrapplingGrade')
bgrapplinggrade = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterB}, {"DefensiveGrade":1, "_id":0}).distinct('DefensiveGrade')
bdefensegrade = xox[0]


xox = db.WEBFighterData.find({"fighterCode":fighterA}, {"TakedownRate":1, "_id":0}).distinct('TakedownRate')
atdrate = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterA}, {"StrikeLandRate":1, "_id":0}).distinct('StrikeLandRate')
astrikingrate = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterA}, {"KickLandRate":1, "_id":0}).distinct('KickLandRate')
akickingrate = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterA}, {"PunchLandRate":1, "_id":0}).distinct('PunchLandRate')
apunchingrate = xox[0]



xox = db.WEBFighterData.find({"fighterCode":fighterB}, {"TakedownRate":1, "_id":0}).distinct('TakedownRate')
btdrate = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterB}, {"StrikeLandRate":1, "_id":0}).distinct('StrikeLandRate')
bstrikingrate = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterB}, {"KickLandRate":1, "_id":0}).distinct('KickLandRate')
bkickingrate = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterB}, {"PunchLandRate":1, "_id":0}).distinct('PunchLandRate')
bpunchingrate = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterA}, {"KnockdownsPer25":1, "_id":0}).distinct('KnockdownsPer25')
aknockdownrate = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterA}, {"StunsPer25":1, "_id":0}).distinct('StunsPer25')
astunrate = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterB}, {"KnockdownsPer25":1, "_id":0}).distinct('KnockdownsPer25')
bknockdownrate = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterB}, {"StunsPer25":1, "_id":0}).distinct('StunsPer25')
bstunrate = xox[0]


xox = db.WEBFighterData.find({"fighterCode":fighterA}, {"TimesKnockedDownPer25":1, "_id":0}).distinct('TimesKnockedDownPer25')
atimesknockdownrate = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterA}, {"TimesStunnedPer25":1, "_id":0}).distinct('TimesStunnedPer25')
atimesstunrate = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterB}, {"TimesKnockedDownPer25":1, "_id":0}).distinct('TimesKnockedDownPer25')
btimesknockdownrate = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterB}, {"TimesStunnedPer25":1, "_id":0}).distinct('TimesStunnedPer25')
btimesstunrate = xox[0]


xox = db.WEBFighterData.find({"fighterCode":fighterA}, {"SubAttemptsPer25":1, "_id":0}).distinct('SubAttemptsPer25')
asubrate = xox[0]

xox = db.WEBFighterData.find({"fighterCode":fighterB}, {"SubAttemptsPer25":1, "_id":0}).distinct('SubAttemptsPer25')
bsubrate = xox[0]



mydict = { 
                "fighterCodeA": fighterA,
                "fighterCodeB": fighterB,
                "fighterAURL": fighteraurl,
                "fighterBURL": fighterburl,
                "fighterAIMG": fighteraIMG,
                "fighterBIMG": fighterbIMG,
                "fighterAName": fighteraName,
                "fighterBName": fighterbName,
                "fighterAStance": fighteraStance,
                "fighterBStance": fighterbStance,
                "fighterA1StrikeLanded": a1strikelanded,
                "fighterB1StrikeLanded": b1strikelanded,
                "fighterA2StrikeLanded": a2strikelanded,
                "fighterB2StrikeLanded": b2strikelanded,
                "fighterA3StrikeLanded": a3strikelanded,
                "fighterB3StrikeLanded": b3strikelanded,
                "fighterAHeight": aheight,
                "fighterBHeight": bheight,
                "fighterAFighterGrade": afightergrade,
                "fighterBFighterGrade": bfightergrade,
                "fighterAStrikingGrade": astrikinggrade,
                "fighterBStrikingGrade": bstrikinggrade,
                "fighterAGrapplingGrade": agrapplinggrade,
                "fighterBGrapplingGrade": bgrapplinggrade,
                "fighterADefensiveGrade": adefensegrade,
                "fighterBDefensiveGrade": bdefensegrade,
                "fighterATDRate": atdrate,
                "fighterBTDRate": btdrate,
                "fighterAStrikingRate": astrikinggrade,
                "fighterBStrikingRate": bstrikinggrade,
                "fighterAKickRate": akickingrate,
                "fighterBKickRate": bkickingrate,
                "fighterAPunchRate": apunchingrate,
                "fighterBPunchRate": bpunchingrate,
                "fighterAKnockdownRate": aknockdownrate,
                "fighterBKnockdownRate": bknockdownrate,
                "fighterAStunRate": astunrate,
                "fighterBStunRate": bstunrate,
                "fighterATimesStunnedRate": atimesstunrate,
                "fighterBTimesStunnedRate": btimesstunrate,
                "fighterATimesKnockedDownRate": atimesknockdownrate,
                "fighterBTimesKnockedDownRate": btimesknockdownrate,
                "fighterASUBRate": asubrate,
                "fighterBSUBRate": bsubrate,
                }

webmatchupdata.insert_one(mydict)
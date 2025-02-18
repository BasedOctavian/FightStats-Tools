#Figures out the average stats per each weight class 
import pymongo
import csv
import sqlite3
import random



#Setting Up The Connections To The DB
myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@octc1.d2he2mx.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]
fighterdata = db["FighterData"]
fighternames = db["FighterNames"]
weightclasses = db["WeightClasses"]
wcav = db["WCAV"]
webfighterdata = db["WEBFighterData"]
webfightdata = db["WEBFightData"]





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
allfightcodes = db.Fights.distinct('fightCode')

allwebfighters = db.WEBFighterData.distinct('fighterCode')

webfightdata.drop()

for x in allfightcodes:
    
    
    
    xox = db.Fights.find({"fightCode":x}, {"FightsTracked":1, "_id":0}).distinct('FightsTracked')
    
    #does fighter A exist
    xox = db.Fights.find({"fightCode":x}, {"fighterA":1, "_id":0}).distinct('fighterA')
    fightera = xox[0]
    
    aname = db.FighterNames.find({"fighterCode":fightera}, {"fighterName":1, "_id":0}).distinct('fighterName')
    
    try:
        fighteraName = aname[0]
    except:
        fighteraName = fightera
    
    
    fighteraexist = False
    for y in allwebfighters:
        if y == fightera:
            fighteraexist = True
            
            
    
    
    
    #does fighter B exist 
    xox = db.Fights.find({"fightCode":x}, {"fighterB":1, "_id":0}).distinct('fighterB')
    fighterb = xox[0]
    
    
    bname = db.FighterNames.find({"fighterCode":fighterb}, {"fighterName":1, "_id":0}).distinct('fighterName')
    
    
    try:
        fighterbName = bname[0]
    except:
        fighterbName = fighterb
    
    
    
    fighterbexist = False
    for y in allwebfighters:
        if y == fighterb:
            fighterbexist = True
            
            
    
              
            
    #Create the blank doc
    
    if fighteraexist == True and fighterbexist == True:
        fightera = fightera.replace(" ", "-")
        fighteraurl = 'https://www.fightstats.xyz/fighterdata/' + fightera.lower()
        fighterb = fighterb.replace(" ", "-")
        fighterburl = 'https://www.fightstats.xyz/fighterdata/' + fighterb.lower()
    
    
    if fighteraexist == True and fighterbexist == False:
        fightera = fightera.replace(" ", "-")
        fighteraurl = 'https://www.fightstats.xyz/fighterdata/' + fightera.lower()
        fighterburl = 'https://www.fightstats.xyz/fighterinfo/' + fighterbName.lower().replace(" ", "-")
        
        
    if fighteraexist == False and fighterbexist == True:
        fighteraurl = 'https://www.fightstats.xyz/fighterinfo/' + fighteraName.lower().replace(" ", "-")
        fighterb = fighterb.replace(" ", "-")
        fighterburl = 'https://www.fightstats.xyz/fighterdata/' + fighterb.lower()
        
        
    if fighteraexist == False and fighterbexist == False:
        fighteraurl = 'https://www.fightstats.xyz/fighterinfo/' + fighteraName.lower().replace(" ", "-")
        fighterburl = 'https://www.fightstats.xyz/fighterinfo/' + fighterbName.lower().replace(" ", "-")
     
     
    xox = db.Fights.find({"fightCode":x}, {"eventCode":1, "_id":0}).distinct('eventCode')
    xoxy = db.Events.find({"EventCode":xox[0]}, {"EventName":1, "_id":0}).distinct('EventName')
    eventCode = xox[0].replace(" ", "-")
    eventCode = 'https://www.fightstats.xyz/search?q=' + eventCode.lower()
    
    eventName = xoxy[0]
    
    xox = db.Fights.find({"fightCode":x}, {"eventCode":1, "_id":0}).distinct('eventCode')
    eventCode2 = xox[0]
    xox = db.Events.find({"EventCode":eventCode2}, {"Date":1, "_id":0}).distinct('Date')
    fightDate = xox[0]
    
    
    
    
    xox = db.Fights.find({"fightCode":x}, {"actualRounds":1, "_id":0}).distinct('actualRounds')
    actualRounds = xox[0] 
    
    xox = db.Fights.find({"fightCode":x}, {"finalRoundTime":1, "_id":0}).distinct('finalRoundTime')
    roundTime = xox[0] 
    
    xox = db.Fights.find({"fightCode":x}, {"methodOfFinish":1, "_id":0}).distinct('methodOfFinish')
    methodOfFinish = xox[0] 
    
    xox = db.Fights.find({"fightCode":x}, {"weightClass":1, "_id":0}).distinct('weightClass')
    weightClass = xox[0] 
    
    
    
    xox = db.Fights.find({"fightCode":x}, {"isTitleFight":1, "_id":0}).distinct('isTitleFight')
    isTitleFight = xox[0] 
        
        
    ard1 = db.Fights.find({"fightCode":x}, {"Around1StrikesLanded":1, "_id":0}).distinct('Around1StrikesLanded')
    ard2 = db.Fights.find({"fightCode":x}, {"Around2StrikesLanded":1, "_id":0}).distinct('Around2StrikesLanded')
    ard3 = db.Fights.find({"fightCode":x}, {"Around3StrikesLanded":1, "_id":0}).distinct('Around3StrikesLanded')
    ard4 = db.Fights.find({"fightCode":x}, {"Around4StrikesLanded":1, "_id":0}).distinct('Around4StrikesLanded')
    ard5 = db.Fights.find({"fightCode":x}, {"Around5StrikesLanded":1, "_id":0}).distinct('Around5StrikesLanded')
    
    
    brd1 = db.Fights.find({"fightCode":x}, {"Bround1StrikesLanded":1, "_id":0}).distinct('Bround1StrikesLanded')
    brd2 = db.Fights.find({"fightCode":x}, {"Bround2StrikesLanded":1, "_id":0}).distinct('Bround2StrikesLanded')
    brd3 = db.Fights.find({"fightCode":x}, {"Bround3StrikesLanded":1, "_id":0}).distinct('Bround3StrikesLanded')
    brd4 = db.Fights.find({"fightCode":x}, {"Bround4StrikesLanded":1, "_id":0}).distinct('Bround4StrikesLanded')
    brd5 = db.Fights.find({"fightCode":x}, {"Bround5StrikesLanded":1, "_id":0}).distinct('Bround5StrikesLanded')
    
    
    try:
        ard1s = ard1[0]
    except:
        ard1s = 0
        
    try:
        ard2s = ard2[0]
    except:
        ard2s = 0
        
    try:
        ard3s = ard3[0]
    except:
        ard3s = 0
        
    try:
        ard4s = ard4[0]
    except:
        ard4s = 0
        
    try:
        ard5s = ard5[0]
    except:
        ard5s = 0
        
        
    try:
        brd1s = brd1[0]
    except:
        brd1s = 0
        
    try:
        brd2s = brd2[0]
    except:
        brd2s = 0
        
    try:
        brd3s = brd3[0]
    except:
        brd3s = 0
        
    try:
        brd4s = brd4[0]
    except:
        brd4s = 0
        
    try:
        brd5s = brd5[0]
    except:
        brd5s = 0    
        
        
    
    xox = db.Fights.find({"fightCode":x}, {"ANumberOfKnockDowns":1, "_id":0}).distinct('ANumberOfKnockDowns')
    
    try:
        anumofknockdowns = xox[0]
    except:
        anumofknockdowns = "N/A"
    
    xox = db.Fights.find({"fightCode":x}, {"BNumberOfKnockDowns":1, "_id":0}).distinct('BNumberOfKnockDowns')
    
    
    try:
        bnumofknockdowns = xox[0]
    except:
        bnumofknockdowns = "N/A"
    
    xox = db.Fights.find({"fightCode":x}, {"ANumberOfStuns":1, "_id":0}).distinct('ANumberOfStuns')
    
    
    try:
        anumofstuns = xox[0]
    except:
        anumofstuns = "N/A"
    
    xox = db.Fights.find({"fightCode":x}, {"BNumberOfStuns":1, "_id":0}).distinct('BNumberOfStuns')
    
    
    try:
        bnumofstuns = xox[0]
    except:
        bnumofstuns = "N/A"
    
    xox = db.Fights.find({"fightCode":x}, {"ATotalJabsMade":1, "_id":0}).distinct('ATotalJabsMade')
    
    
    try:
        ajabs = xox[0]
    except:
        ajabs = 0
    
    xox = db.Fights.find({"fightCode":x}, {"BTotalJabsMade":1, "_id":0}).distinct('BTotalJabsMade')
    
    
    try:
        bjabs = xox[0]
    except:
        bjabs = 0
    
    xox = db.Fights.find({"fightCode":x}, {"ATotalStraightsMade":1, "_id":0}).distinct('ATotalStraightsMade')
    
    
    try:
        astraights = xox[0]
    except:
        astraights = 0
    
    
    xox = db.Fights.find({"fightCode":x}, {"BTotalStraightsMade":1, "_id":0}).distinct('BTotalStraightsMade')
    
    
    try:
        bstraights = xox[0]
    except:
        bstraights = 0
    
    
    xox = db.Fights.find({"fightCode":x}, {"ATotalHooksMade":1, "_id":0}).distinct('ATotalHooksMade')
    
    
    try:
        ahooks = xox[0]
    except:
        ahooks = 0
    
    
    xox = db.Fights.find({"fightCode":x}, {"BTotalHooksMade":1, "_id":0}).distinct('BTotalHooksMade')
    
    try:
        bhooks = xox[0]
    except:
        bhooks = 0
    
    
    xox = db.Fights.find({"fightCode":x}, {"ATotalUppercutsMade":1, "_id":0}).distinct('ATotalUppercutsMade')

    
    
    try:
        auppercuts = xox[0]
    except:
        auppercuts = 0
    
    
    xox = db.Fights.find({"fightCode":x}, {"BTotalUppercutsMade":1, "_id":0}).distinct('BTotalUppercutsMade')
    
    try:
        buppercuts = xox[0]
    except:
        buppercuts = 0
    
    
    xox = db.Fights.find({"fightCode":x}, {"ATotalLegKickMake":1, "_id":0}).distinct('ATotalLegKickMake')  
    
    try:
        alegkicks = xox[0]
    except:
        alegkicks = 0
    
    
    xox = db.Fights.find({"fightCode":x}, {"BTotalLegKickMake":1, "_id":0}).distinct('BTotalLegKickMake')
    
    try:
        blegkicks = xox[0]
    except:
        blegkicks = 0
    
    
    xox = db.Fights.find({"fightCode":x}, {"ATotalBodyKickMake":1, "_id":0}).distinct('ATotalBodyKickMake')
    
    try:
        abodykicks = xox[0]
    except:
        abodykicks = 0
        
    
    xox = db.Fights.find({"fightCode":x}, {"BTotalBodyKickMake":1, "_id":0}).distinct('BTotalBodyKickMake')
    
    try:
        bbodykicks = xox[0]
    except:
        bbodykicks = 0
    
    
    xox = db.Fights.find({"fightCode":x}, {"ATotalHeadKickMake":1, "_id":0}).distinct('ATotalHeadKickMake')
    
    try:
        aheadkicks = xox[0]
    except:
        aheadkicks = 0
    
    
    xox = db.Fights.find({"fightCode":x}, {"BTotalHeadKickMake":1, "_id":0}).distinct('BTotalHeadKickMake')
    
    
    try:
        bheadkicks = xox[0]
    except:
        bheadkicks = 0
        
    
    xox = db.Fights.find({"fightCode":x}, {"ATotalOverhandsMade":1, "_id":0}).distinct('ATotalOverhandsMade')
    
    try:
        aoverhand = xox[0]
    except:
        aoverhand = 0
    
    xox = db.Fights.find({"fightCode":x}, {"BTotalOverhandsMade":1, "_id":0}).distinct('BTotalOverhandsMade')
    
    try:
        boverhand = xox[0]
    except:
        boverhand = 0
    
    
    xox = db.Fights.find({"fightCode":x}, {"ATotalTakedownsAttempted":1, "_id":0}).distinct('ATotalTakedownsAttempted')
    
    try:
        atdattempt = xox[0]
    except:
        atdattempt = "N/A"
    
    
    xox = db.Fights.find({"fightCode":x}, {"BTotalTakedownsAttempted":1, "_id":0}).distinct('BTotalTakedownsAttempted')
    
    try:
        btdattempt = xox[0]
    except:
        btdattempt = "N/A"
    
    
    xox = db.Fights.find({"fightCode":x}, {"ATotalTakedownsMade":1, "_id":0}).distinct('ATotalTakedownsMade')
    
    
    try:
        atdmake = xox[0]
    except:
        atdmake = 0
    
    xox = db.Fights.find({"fightCode":x}, {"BTotalTakedownsMade":1, "_id":0}).distinct('BTotalTakedownsMade')
    
    try:
        btdmake = xox[0]
    except:
        btdmake = 0
    
    
    if atdmake > 0 :
        temp = (atdmake / atdattempt) * 100
        temp = round(temp, 1)
        atdrate = str(temp) + "%"
        
    else:
        atdrate = "0%"
        
        
    if btdmake > 0 and btdmake != "N/A":
        temp = (btdmake / btdattempt) * 100
        temp = round(temp, 1)
        btdrate = str(temp) + "%"
        
    else:
        btdrate = "0%"
    
    
    xox = db.Fights.find({"fightCode":x}, {"ATotalSubmissionsAttempted":1, "_id":0}).distinct('ATotalSubmissionsAttempted')
    
    try:
        asubattempts = xox[0]
    except:
        asubattempts = "N/A"
    
    
    xox = db.Fights.find({"fightCode":x}, {"BTotalSubmissionsAttempted":1, "_id":0}).distinct('BTotalSubmissionsAttempted')
    
    try:
        bsubattempts = xox[0]
    except:
        bsubattempts = "N/A"
    
    #Put the new punch, kick, and strike land percent code and try & except statements as well
    
    
    astance1 = db.Fights.find({"fightCode":x}, {"AStance":1, "_id":0}).distinct('AStance')
    bstance1 = db.Fights.find({"fightCode":x}, {"BStance":1, "_id":0}).distinct('BStance')
        
    try:
        astance2 = astance1[0]
       
    except:
        astance2 = ""
        
    try:
        bstance2 = bstance1[0]
       
    except:
        bstance2 = ""
       
    number = random.randint(1000,9999)
    fightname = fighteraName + " vs " + fighterbName + " " + eventName
           
    
    if weightClass == "WomensFlyweight":
        weightClass = "Women's Flyweight"
        
    if weightClass == "WomensStrawweight":
        weightClass = "Women's Strawweight"
        
    if weightClass == "WomensBantamweight":
        weightClass = "Women's Bantamweight"
        
    if weightClass == "WomensFeatherweight":
        weightClass = "Women's Featherweight"
    
    
    #Get High Impact Strike Totals
    ahighround1 = (float(aheadkicks) * 0.9) + (float(abodykicks) * 0.6) + (float(alegkicks) * 0.2) + (float(astraights) * 0.4) + (float(ahooks) * 0.85) + (float(aoverhand) * 0.85) + (float(auppercuts) * 0.90) 
    ahighround1 = int(round(ahighround1))
    
    bhighround1 = (float(bheadkicks) * 0.9) + (float(bbodykicks) * 0.6) + (float(blegkicks) * 0.2) + (float(bstraights) * 0.4) + (float(bhooks) * 0.85) + (float(boverhand) * 0.85) + (float(buppercuts) * 0.90) 
    bhighround1 = int(round(bhighround1))
    
    atotalstrikes = ard1s + ard2s + ard3s + ard4s + ard5s
    btotalstrikes = brd1s + brd2s + brd3s + brd4s + brd5s 
    
    

    #Fighter A Stance Stats
    
    try:
        tempName = bstance2 + "Opp" + "Jabs"
    except:
        tempName = 'Empty'
    xox = db.WEBFighterData.find({"fighterCode":fightera}, {tempName:1, "_id":0}).distinct(tempName)
    try:
        db.WEBFighterData.update_one({"fighterCode":fightera}, {"$set": {tempName: ajabs + xox[0]}})
    except:
        tempName = 'Empty'
    try:
        tempName = bstance2 + "Opp" + "Straights"
    except:
        tempName = 'Empty'
    xox = db.WEBFighterData.find({"fighterCode":fightera}, {tempName:1, "_id":0}).distinct(tempName)
    try:
        db.WEBFighterData.update_one({"fighterCode":fightera}, {"$set": {tempName: astraights + xox[0]}})
    except:
        tempName = 'Empty'
    try:
        tempName = bstance2 + "Opp" + "Hooks"
    except:
        tempName = 'Empty'
    xox = db.WEBFighterData.find({"fighterCode":fightera}, {tempName:1, "_id":0}).distinct(tempName)
    try:
        db.WEBFighterData.update_one({"fighterCode":fightera}, {"$set": {tempName: ahooks + xox[0]}})
    except:
        tempName = 'Empty'
    try:
        tempName = bstance2 + "Opp" + "Uppercuts"
    except:
        tempName = 'Empty'
    xox = db.WEBFighterData.find({"fighterCode":fightera}, {tempName:1, "_id":0}).distinct(tempName)
    try:
        db.WEBFighterData.update_one({"fighterCode":fightera}, {"$set": {tempName: auppercuts + xox[0]}})
    except:
        tempName = 'Empty'
    try:
        tempName = bstance2 + "Opp" + "LegKicks"
    except:
        tempName = 'Empty'
    xox = db.WEBFighterData.find({"fighterCode":fightera}, {tempName:1, "_id":0}).distinct(tempName)
    try:
        db.WEBFighterData.update_one({"fighterCode":fightera}, {"$set": {tempName: alegkicks + xox[0]}})
    except:
        tempName = 'Empty'
    try:
        tempName = bstance2 + "Opp" + "BodyKicks"
    except:
        tempName = 'Empty'
    xox = db.WEBFighterData.find({"fighterCode":fightera}, {tempName:1, "_id":0}).distinct(tempName)
    try:
        db.WEBFighterData.update_one({"fighterCode":fightera}, {"$set": {tempName: abodykicks + xox[0]}})
    except:
        tempName = 'Empty'
    try:
        tempName = bstance2 + "Opp" + "HeadKicks"
    except:
        tempName = 'Empty'
    xox = db.WEBFighterData.find({"fighterCode":fightera}, {tempName:1, "_id":0}).distinct(tempName)
    try:
        db.WEBFighterData.update_one({"fighterCode":fightera}, {"$set": {tempName: aheadkicks + xox[0]}})
    except:
        tempName = 'Empty'
    try:
        tempName = bstance2 + "Opp" + "Overhands"
    except:
        tempName = 'Empty'
    xox = db.WEBFighterData.find({"fighterCode":fightera}, {tempName:1, "_id":0}).distinct(tempName)
    try:
        db.WEBFighterData.update_one({"fighterCode":fightera}, {"$set": {tempName: aoverhand + xox[0]}})
    except:
        tempName = 'Empty'
    
    
    
    
    #Fighter B Stance Stats
    
    try:
        tempName = astance2 + "Opp" + "Jabs"
    except:
        tempName = 'Empty'
    xox = db.WEBFighterData.find({"fighterCode":fighterb}, {tempName:1, "_id":0}).distinct(tempName)
    try:
        db.WEBFighterData.update_one({"fighterCode":fighterb}, {"$set": {tempName: bjabs + xox[0]}})
    except:
        tempName = 'Empty'
    try:
        tempName = astance2 + "Opp" + "Straights"
    except:
        tempName = 'Empty'
    xox = db.WEBFighterData.find({"fighterCode":fighterb}, {tempName:1, "_id":0}).distinct(tempName)
    try:
        db.WEBFighterData.update_one({"fighterCode":fighterb}, {"$set": {tempName: bstraights + xox[0]}})
    except:
        tempName = 'Empty'
    try:
        tempName = astance2 + "Opp" + "Hooks"
    except:
        tempName = 'Empty'
    xox = db.WEBFighterData.find({"fighterCode":fighterb}, {tempName:1, "_id":0}).distinct(tempName)
    try:
        db.WEBFighterData.update_one({"fighterCode":fighterb}, {"$set": {tempName: bhooks + xox[0]}})
    except:
        tempName = 'Empty'
    try:
        tempName = astance2 + "Opp" + "Uppercuts"
    except:
        tempName = 'Empty'
    xox = db.WEBFighterData.find({"fighterCode":fighterb}, {tempName:1, "_id":0}).distinct(tempName)
    try:
        db.WEBFighterData.update_one({"fighterCode":fighterb}, {"$set": {tempName: buppercuts + xox[0]}})
    except:
        tempName = 'Empty'
    try:
        tempName = astance2 + "Opp" + "LegKicks"
    except:
        tempName = 'Empty'
    xox = db.WEBFighterData.find({"fighterCode":fighterb}, {tempName:1, "_id":0}).distinct(tempName)
    try:
        db.WEBFighterData.update_one({"fighterCode":fighterb}, {"$set": {tempName: blegkicks + xox[0]}})
    except:
        tempName = 'Empty'
    try:
        tempName = astance2 + "Opp" + "BodyKicks"
    except:
        tempName = 'Empty'
    xox = db.WEBFighterData.find({"fighterCode":fighterb}, {tempName:1, "_id":0}).distinct(tempName)
    try:
        db.WEBFighterData.update_one({"fighterCode":fighterb}, {"$set": {tempName: bbodykicks + xox[0]}})
    except:
        tempName = 'Empty'
    try:
        tempName = astance2 + "Opp" + "HeadKicks"
    except:
        tempName = 'Empty'
    xox = db.WEBFighterData.find({"fighterCode":fighterb}, {tempName:1, "_id":0}).distinct(tempName)
    try:
        db.WEBFighterData.update_one({"fighterCode":fighterb}, {"$set": {tempName: bheadkicks + xox[0]}})
    except:
        tempName = 'Empty'
    try:
        tempName = astance2 + "Opp" + "Overhands"
    except:
        tempName = 'Empty'
    xox = db.WEBFighterData.find({"fighterCode":fighterb}, {tempName:1, "_id":0}).distinct(tempName)
    try:
        db.WEBFighterData.update_one({"fighterCode":fighterb}, {"$set": {tempName: boverhand + xox[0]}})
    except:
        tempName = 'Empty'
    
    
    
    mydict = { 
            "fightCode": x,
            "eventCode": eventCode,
            "fightDate": fightDate,
            "fighterAName": fighteraName,
            "fighterBName": fighterbName,
            "containsName": fighteraName + " " + fighterbName,
            "fightName": fightname,
            "fighterA": fighteraurl,
            "fighterB": fighterburl,
            "Rounds": actualRounds,
            "Time": roundTime,
            "methodOfFinish": methodOfFinish,
            "weightClass": weightClass,
            "isTitleFight": isTitleFight,
            "Around1StrikesLanded": ard1s,
            "Around2StrikesLanded": ard2s,
            "Around3StrikesLanded": ard3s,
            "Around4StrikesLanded": ard4s,
            "Around5StrikesLanded": ard5s,
            "Bround1StrikesLanded": brd1s,
            "Bround2StrikesLanded": brd2s,
            "Bround3StrikesLanded": brd3s,
            "Bround4StrikesLanded": brd4s,
            "Bround5StrikesLanded": brd5s,
            "anumofknockdowns": anumofknockdowns,
            "bnumofknockdowns": bnumofknockdowns,
            "anumofstuns": anumofstuns,
            "bnumofstuns": bnumofstuns,
            "ajabs": ajabs,
            "bjabs": bjabs,
            "astraights": astraights,
            "bstraights": bstraights,
            "ahooks": ahooks,
            "bhooks": bhooks,
            "auppercuts": auppercuts,
            "buppercuts": buppercuts,
            "alegkick": alegkicks,
            "blegkick": blegkicks,
            "abodykick": abodykicks,
            "bbodykick": bbodykicks,
            "aheadkick": aheadkicks,
            "bheadkick": bheadkicks,
            "aoverhands": aoverhand,
            "boverhands": boverhand,
            "atdattempt": atdattempt,
            "btdattempt": btdattempt,
            "atdmake": atdmake,
            "btdmake": btdmake,
            "atdrate": atdrate,
            "btdrate": btdrate,
            "asubattempt": asubattempts,
            "bsubattempt": bsubattempts,
            "astance": astance2,
            "bstance": bstance2,
            "AHighImpact": ahighround1,
            "BHighImpact": bhighround1
            }
    
    webfightdata.insert_one(mydict)
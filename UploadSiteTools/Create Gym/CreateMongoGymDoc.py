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
webgymdata = db["WEBGymData"]

webgymdata.drop()




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
allgymcodes = db.Gyms.distinct('gymCode')



for x in allgymcodes:
    
    
    
    xox = db.Gyms.find({"gymCode":x}, {"FightsTracked":1, "_id":0}).distinct('FightsTracked')
    fightsTracked = xox[0]
    if fightsTracked > 6:
        
    
        xox = db.Gyms.find({"gymCode":x}, {"gymName":1, "_id":0}).distinct('gymName')
        gymName = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"gymState":1, "_id":0}).distinct('gymState')
        gymState = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"gymCountry":1, "_id":0}).distinct('gymCountry')
        gymCountry = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"gymWins":1, "_id":0}).distinct('gymWins')
        gymWins = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"gymLoss":1, "_id":0}).distinct('gymLoss')
        gymLoss = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"KO":1, "_id":0}).distinct('KO')
        KO = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"TKO":1, "_id":0}).distinct('TKO')
        TKO = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"SUB":1, "_id":0}).distinct('SUB')
        SUB = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"DEC":1, "_id":0}).distinct('DEC')
        DEC = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"TotalTDMake":1, "_id":0}).distinct('TotalTDMake')
        TotalTDMake = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"TotalTDAttempt":1, "_id":0}).distinct('TotalTDAttempt')
        TotalTDAttempt = xox[0]
        
        temp = (TotalTDMake / TotalTDAttempt) * 100
        temp = round(temp, 1)
        tdrate = str(temp)
        tdrate = tdrate + "%"
        
        xox = db.Gyms.find({"gymCode":x}, {"TotalJabAttempt":1, "_id":0}).distinct('TotalJabAttempt')
        TotalJabAttempt = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"TotalStraightAttempt":1, "_id":0}).distinct('TotalStraightAttempt')
        TotalStraightAttempt = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"TotalHookAttempt":1, "_id":0}).distinct('TotalHookAttempt')
        TotalHookAttempt = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"TotalUppercutAttempt":1, "_id":0}).distinct('TotalUppercutAttempt')
        TotalUppercutAttempt = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"TotalHeadKickAttempt":1, "_id":0}).distinct('TotalHeadKickAttempt')
        TotalHeadKickAttempt = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"TotalBodyKickAttempt":1, "_id":0}).distinct('TotalBodyKickAttempt')
        TotalBodyKickAttempt = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"TotalLegKickAttempt":1, "_id":0}).distinct('TotalLegKickAttempt')
        TotalLegKickAttempt = xox[0]
        
        totalstrikeattempts = (TotalLegKickAttempt + TotalBodyKickAttempt + TotalHeadKickAttempt + TotalUppercutAttempt + TotalHookAttempt + TotalStraightAttempt + TotalJabAttempt)
        
        temp = (TotalJabAttempt / totalstrikeattempts) * 100
        temp = round(temp, 1)
        jabrate = str(temp) + "%"
        
        temp = (TotalStraightAttempt / totalstrikeattempts) * 100
        temp = round(temp, 1)
        straightrate = str(temp) + "%"
        
        temp = (TotalHookAttempt / totalstrikeattempts) * 100
        temp = round(temp, 1)
        hookrate = str(temp) + "%"
        
        temp = (TotalUppercutAttempt / totalstrikeattempts) * 100
        temp = round(temp, 1)
        uppercutrate = str(temp) + "%"
        
        temp = (TotalHeadKickAttempt / totalstrikeattempts) * 100
        temp = round(temp, 1)
        headkickrate = str(temp) + "%"
        
        temp = (TotalBodyKickAttempt / totalstrikeattempts) * 100
        temp = round(temp, 1)
        bodykickrate = str(temp) + "%"
        
        temp = (TotalLegKickAttempt / totalstrikeattempts) * 100
        temp = round(temp, 1)
        legkickrate = str(temp) + "%"
        
        
        
        
        xox = db.Gyms.find({"gymCode":x}, {"JabsAbsorbed":1, "_id":0}).distinct('JabsAbsorbed')
        JabsAbsorbed = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"StraightsAbsorbed":1, "_id":0}).distinct('StraightsAbsorbed')
        StraightsAbsorbed = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"HooksAbsorbed":1, "_id":0}).distinct('HooksAbsorbed')
        HooksAbsorbed = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"UppercutsAbsorbed":1, "_id":0}).distinct('UppercutsAbsorbed')
        UppercutsAbsorbed = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"LegKicksAbsorbed":1, "_id":0}).distinct('LegKicksAbsorbed')
        LegKicksAbsorbed = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"BodyKicksAbsorbed":1, "_id":0}).distinct('BodyKicksAbsorbed')
        BodyKicksAbsorbed = xox[0]
        
        xox = db.Gyms.find({"gymCode":x}, {"HeadKicksAbsorbed":1, "_id":0}).distinct('HeadKicksAbsorbed')
        HeadKicksAbsorbed = xox[0]
        
        
        totalstrikesabsorbed = (JabsAbsorbed + StraightsAbsorbed + HooksAbsorbed + UppercutsAbsorbed + LegKicksAbsorbed + HeadKicksAbsorbed + BodyKicksAbsorbed)
        
        
        temp = (JabsAbsorbed / totalstrikesabsorbed) * 100
        temp = round(temp, 1)
        jababsrate = str(temp) + "%"
        
        temp = (StraightsAbsorbed / totalstrikesabsorbed) * 100
        temp = round(temp, 1)
        straightsabsrate = str(temp) + "%"
        
        temp = (HooksAbsorbed / totalstrikesabsorbed) * 100
        temp = round(temp, 1)
        hooksabsrate = str(temp) + "%"
        
        temp = (UppercutsAbsorbed / totalstrikesabsorbed) * 100
        temp = round(temp, 1)
        uppercutsabsrate = str(temp) + "%"
        
        temp = (LegKicksAbsorbed / totalstrikesabsorbed) * 100
        temp = round(temp, 1)
        legkicksabsrate = str(temp) + "%"
        
        temp = (BodyKicksAbsorbed / totalstrikesabsorbed) * 100
        temp = round(temp, 1)
        bodykicksabsrate = str(temp) + "%"
        
        temp = (HeadKicksAbsorbed / totalstrikesabsorbed) * 100
        temp = round(temp, 1)
        headkicksabsrate = str(temp) + "%"
        
             
        temp = (KO / fightsTracked) * 100
        temp = round(temp, 1)
        KORate = str(temp) + "%"
        
        temp = (TKO / fightsTracked) * 100
        temp = round(temp, 1)
        TKORate = str(temp) + "%"
        
        temp = (SUB / fightsTracked) * 100
        temp = round(temp, 1)
        SUBRate = str(temp) + "%"
        
        temp = (DEC / fightsTracked) * 100
        temp = round(temp, 1)
        DECRate = str(temp) + "%"
        
        
        
        temp = (gymWins / fightsTracked) * 100
        temp = round(temp, 1)
        WINRate = str(temp) + "%"
        
        temp = (gymLoss / fightsTracked) * 100
        temp = round(temp, 1)
        LOSSRate = str(temp) + "%"
        
        
        
        mydict = { 
                "gymCode": x,
                "gymName": gymName,
                "gymState": gymState,
                "gymCountry": gymCountry,
                "gymWins": WINRate,
                "gymLoss": LOSSRate,
                "KO": KORate,
                "TKO": TKORate,
                "SUB": SUBRate,
                "DEC": DECRate,
                "jabRate": jabrate,
                "straightRate": straightrate,
                "hookRate": hookrate,
                "uppercutRate": uppercutrate,
                "legKickRate": legkickrate,
                "bodyKickRate": bodykickrate,
                "headKickRate": headkickrate,
                "jabAbsRate": jababsrate,
                "straightAbsRate": straightsabsrate,
                "hookAbsRate": hooksabsrate,
                "uppercutAbsRate": uppercutsabsrate,
                "legKickAbsRate": legkicksabsrate,
                "bodyKickAbsRate": bodykicksabsrate,
                "headKickAbsRate": headkicksabsrate,
                }
        if(gymName == 'UFC Performance Institute'):
            print("UFCPI")
        else:
            webgymdata.insert_one(mydict)
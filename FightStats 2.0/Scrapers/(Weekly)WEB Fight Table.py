#Figures out the average stats per each weight class 
    import pymongo
import re
import csv
import sqlite3
import random
from unidecode import unidecode 

from urllib.parse import urlparse, parse_qs

from datetime import datetime

#Setting Up The Connections To The DB
myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@octc1.d2he2mx.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]
fighterdata = db["FighterData"]
fighternames = db["FighterNames"]
weightclasses = db["WeightClasses"]
wcav = db["WCAV"]
webnodatafights = db["WEBNoDataFights"]
webfightdata = db["WEBFightData"]

webfighterdata = db["WEBFighterData"]

webeventdata = db["WEBEventData"]

webnodatafights.drop()

dontfightcodes = []

#Loops through each fight with stats first & assigns code of fightera-fighterb-date and a link to fighter a, fighterb, the fight & event & puts all the codes in a list for fights to skip & has a string that says 'View Stats' and adds to mongo

def clean_name(name):
    # Remove all special characters except spaces
    cleaned_name = re.sub(r'[^\w\s]', '', name)
    # Convert the name to title case
    cleaned_name = cleaned_name.title()
    return cleaned_name


def month_to_number(month_name):
    months = {
        'January': '1',
        'February': '2',
        'March': '3',
        'April': '4',
        'May': '5',
        'June': '6',
        'July': '7',
        'August': '8',
        'September': '9',
        'October': '10',
        'November': '11',
        'December': '12'
    }
    return months[month_name]


allwebfights = db.WEBFightData.distinct('fightCode')
allfights = db.Fights.distinct('fightCode')
allevents = db.Events.distinct('EventCode')
allnodatafights = db.WEBNoDataFights.distinct('_id')

alleventdata = db.WEBEventData.distinct('eventName')


for x in allwebfights:
    
    xox = db.WEBFightData.find({"fightCode":x}, {"Rounds":1, "_id":0}).distinct('Rounds')
    fightrounds = xox[0]
    
    xox = db.WEBFightData.find({"fightCode":x}, {"methodOfFinish":1, "_id":0}).distinct('methodOfFinish')
    fightfinish = xox[0]
    
    if fightfinish in ['UD', 'SD', 'Maj Dec']:
        fightfinish = "Decision"
    
    xox = db.WEBFightData.find({"fightCode":x}, {"fighterAName":1, "_id":0}).distinct('fighterAName')
    fighteraname = xox[0]
    xox = db.WEBFightData.find({"fightCode":x}, {"fighterBName":1, "_id":0}).distinct('fighterBName')
    fighterbname = xox[0]
    
    xox = db.WEBFightData.find({"fightCode":x}, {"fightName":1, "_id":0}).distinct('fightName')
    fightnamecode = xox[0]
    
    fightpageurl = 'https://www.fightstats.xyz/fightdata/' + fightnamecode
    
    xox = db.WEBFightData.find({"fightCode":x}, {"fighterA":1, "_id":0}).distinct('fighterA')
    fighteralink = xox[0]
    xox = db.WEBFightData.find({"fightCode":x}, {"fighterB":1, "_id":0}).distinct('fighterB')
    fighterblink = xox[0]
    
    #Get Total Strikes
    xox = db.WEBFightData.find({"fightCode":x}, {"Around1StrikesLanded":1, "_id":0}).distinct('Around1StrikesLanded')
    ard1 = xox[0]
    xox = db.WEBFightData.find({"fightCode":x}, {"Around2StrikesLanded":1, "_id":0}).distinct('Around2StrikesLanded')
    ard2 = xox[0]
    xox = db.WEBFightData.find({"fightCode":x}, {"Around3StrikesLanded":1, "_id":0}).distinct('Around3StrikesLanded')
    ard3 = xox[0]
    xox = db.WEBFightData.find({"fightCode":x}, {"Around4StrikesLanded":1, "_id":0}).distinct('Around4StrikesLanded')
    ard4 = xox[0]
    xox = db.WEBFightData.find({"fightCode":x}, {"Around5StrikesLanded":1, "_id":0}).distinct('Around5StrikesLanded')
    ard5 = xox[0]
    
    #Get Total Strikes
    xox = db.WEBFightData.find({"fightCode":x}, {"Bround1StrikesLanded":1, "_id":0}).distinct('Bround1StrikesLanded')
    brd1 = xox[0]
    xox = db.WEBFightData.find({"fightCode":x}, {"Bround2StrikesLanded":1, "_id":0}).distinct('Bround2StrikesLanded')
    brd2 = xox[0]
    xox = db.WEBFightData.find({"fightCode":x}, {"Bround3StrikesLanded":1, "_id":0}).distinct('Bround3StrikesLanded')
    brd3 = xox[0]
    xox = db.WEBFightData.find({"fightCode":x}, {"Bround4StrikesLanded":1, "_id":0}).distinct('Bround4StrikesLanded')
    brd4 = xox[0]
    xox = db.WEBFightData.find({"fightCode":x}, {"Bround5StrikesLanded":1, "_id":0}).distinct('Bround5StrikesLanded')
    brd5 = xox[0]
    
    #Get Total TD's
    xox = db.WEBFightData.find({"fightCode":x}, {"atdmake":1, "_id":0}).distinct('atdmake')
    atdmake = xox[0]
    xox = db.WEBFightData.find({"fightCode":x}, {"btdmake":1, "_id":0}).distinct('btdmake')
    btdmake = xox[0]
    
    atotalstrikes = ard1 + ard2 + ard3 + ard4 + ard5
    btotalstrikes = brd1 + brd2 + brd3 + brd4 + brd5
    
    xox = db.WEBFightData.find({"fightCode":x}, {"eventCode":1, "_id":0}).distinct('eventCode')
    eventCode2 = xox[0]
    
    query_param = parse_qs(urlparse(eventCode2).query)['q'][0]
    eventurl = 'https://www.fightstats.xyz/event/' + query_param
    
    #Remove champ (c)
    
    if fighteraname.endswith(" (c)"):
        fighteraname = fighteraname[:-3]  # remove the last 3 characters
    else:
        fighteraname = fighteraname  # keep the original string
        
    if fighterbname.endswith(" (c)"):
        fighterbname = fighterbname[:-3]  # remove the last 3 characters
    else:
        fighterbname = fighterbname  # keep the original string
    
    #Remove special characters
    cleanedAname = clean_name(fighteraname) 
    cleanedBname = clean_name(fighterbname) 
    
    for y in allfights:
        if y == x:
            #Get The Event Code
            xox = db.Fights.find({"fightCode":y}, {"eventCode":1, "_id":0}).distinct('eventCode')
            eventCode = xox[0]
    
    #Get the date 
    for u in allevents:
        if u == eventCode:
            xox = db.Events.find({"EventCode":u}, {"Date":1, "_id":0}).distinct('Date')
            eventDate = xox[0]
            
    if cleanedAname.endswith('(C)'):
        cleanedAname = cleanedAname[:-3]
    elif cleanedAname.endswith('(IC)'):
        cleanedAname = cleanedAname[:-4]
            
    if cleanedBname.endswith('(C)'):
            cleanedBname = cleanedBname[:-3]
    elif cleanedBname.endswith('(IC)'):
            cleanedBname = cleanedBname[:-4]
            
    cleanedAname = unidecode(cleanedAname)
    cleanedBname = unidecode(cleanedBname)         
    
    
    newfightcode = cleanedAname.strip() + cleanedBname.strip() + eventDate
    no_space_text = newfightcode.replace(" ", "")
    lowercase_text = no_space_text.lower()
    newfightcode = lowercase_text
    
    dontfightcodes.append(newfightcode)
    
    #Get fighter a & b fighter pages
    
    #Add the entry to mongo
    
    #Does fighter a have a fighter data page or fighter page
    query = {"fighterName": fighteraname}
    result = webfighterdata.find_one(query)
    if result:
        #Get fighter code
        xox = db.WEBFighterData.find({"fighterName":fighteraname}, {"fighterCode":0}).distinct('fighterCode')
        afightercode = xox[0]
        winnerpage = 'https://www.fightstats.xyz/fighterdata/' + afightercode
    else:
        winnerpage = 'https://www.fightstats.xyz/fighter/' + fighteraname.strip()
        
    #Does fighter b have a fighter data page or fighter page
    query = {"fighterName": fighterbname}
    result = webfighterdata.find_one(query)
    if result:
        #Get fighter code
        xox = db.WEBFighterData.find({"fighterName":fighterbname}, {"fighterCode":0}).distinct('fighterCode')
        bfightercode = xox[0]
        loserpage = 'https://www.fightstats.xyz/fighterdata/' + bfightercode
    else:
        loserpage = 'https://www.fightstats.xyz/fighter/' + fighterbname.strip()
    
    
    if fightfinish in ['UD', 'SD', 'Maj Dec']:
        fightfinish = "Decision"
    
    fighteraname = fighteraname.strip()
    fighterbname = fighterbname.strip()
    fighteraname = unidecode(fighteraname)
    fighterbname = unidecode(fighterbname)
    
    
    mydict = {
        "Winner": fighteraname,
        "WinnerPage": winnerpage,
        "Loser": fighterbname,
        "LoserPage": loserpage,
        "WinnerTotalStrikes": atotalstrikes,
        "LoserTotalStrikes": btotalstrikes,
        "WinnerTD": atdmake,
        "LoserTD": btdmake,
        "FightPage": fightpageurl,
        "LabelText": "View Stats",
        "Date": eventDate,
        "Rounds": fightrounds,
        "Result": fightfinish,
    }
    
    webnodatafights.insert_one(mydict)
    print(newfightcode)

#Loops through all the no data fights & if code doesnt exist in the list prior created Creates all the data but no clickable fight page and has a string that says 'No Data' and adds to mongo


for i in alleventdata:
    
    
    xox = db.WEBFightData.find({"fightCode":x}, {"eventCode":1, "_id":0}).distinct('eventCode')
    eventCode2 = xox[0]
    
    
    
    #Get Event Date
    xox = db.WEBEventData.find({"eventName":i}, {"date":0}).distinct('date')
    eventdate = xox[0]
    
    # Split the original string into its components
    month, day, year = eventdate.split()[0], eventdate.split()[1][:-1], eventdate.split()[-1][1:-1]

    # Reformat the components into a new string
    new_date_string = f"{month_to_number(month)}/{day}/{year}"
    
    #Gets the # of fields in the event document
    eventdocfilter = {"eventName": i}
    document = webeventdata.find_one(eventdocfilter)
    document_count = len(document)
    
    document_count = document_count - 7
    fightcount = document_count / 8
    fightcount = fightcount - 1
    
    integer_value = fightcount
    #Loop through the fightcount
    while integer_value >= 0:
        
        fightcount = integer_value
        decimal_string = str(fightcount)
        integer_value = int(float(decimal_string))
        
        #Make the nodatafightcode
        
        print("fight" + str(integer_value) + "WINNER")
        
        #Get Fighter Names
        xox = db.WEBEventData.find({"eventName":i}, {"fight" + str(integer_value) + "WINNER":1, "_id":0}).distinct("fight" + str(integer_value) + "WINNER")
        fighteraname = xox[0]
        
        xox = db.WEBEventData.find({"eventName":i}, {"fight" + str(integer_value) + "LOSER":1, "_id":0}).distinct("fight" + str(integer_value) + "LOSER")
        fighterbname = xox[0]
        
        
        #Get Rounds & Result
        xox = db.WEBEventData.find({"eventName":i}, {"fight" + str(integer_value) + "ROUND":1, "_id":0}).distinct("fight" + str(integer_value) + "ROUND")
        fightround = xox[0]
        
        xox = db.WEBEventData.find({"eventName":i}, {"fight" + str(integer_value) + "METHOD":1, "_id":0}).distinct("fight" + str(integer_value) + "METHOD")
        fightmethod = xox[0]
                
        if fightmethod in ['UD', 'SD', 'Maj Dec']:
            fightmethod = "Decision"
        
        
        #Remove champ (c)
    
        if fighteraname.endswith(" (c)"):
            fighteraname = fighteraname[:-3]  # remove the last 3 characters
        else:
            fighteraname = fighteraname  # keep the original string
        
        if fighterbname.endswith(" (c)"):
            fighterbname = fighterbname[:-3]  # remove the last 3 characters
        else:
            fighterbname = fighterbname  # keep the original string
            
        #Remove special characters
        cleanedAname = clean_name(fighteraname) 
        cleanedBname = clean_name(fighterbname)   
        
        if cleanedAname.endswith('(C)'):
            cleanedAname = cleanedAname[:-3]
        elif cleanedAname.endswith('(IC)'):
            cleanedAname = cleanedAname[:-4]
            
        if cleanedBname.endswith('(C)'):
            cleanedBname = cleanedBname[:-3]
        elif cleanedBname.endswith('(IC)'):
            cleanedBname = cleanedBname[:-4]
            
        cleanedAname = unidecode(cleanedAname)
        cleanedBname = unidecode(cleanedBname)
         
         
        
        try:
                formatted_date = new_date_string[:new_date_string.index('-')]
                new_date_string = formatted_date
        except:
                new_date_string = new_date_string
        
        testfightcode = cleanedAname.strip() + cleanedBname.strip() + new_date_string
           
        if testfightcode in dontfightcodes:
            print('Skipped')
        else:
            
            #Does fighter a have a fighter data page or fighter page
            query = {"fighterName": fighteraname}
            result = webfighterdata.find_one(query)
            if result:
                #Get fighter code
                xox = db.WEBFighterData.find({"fighterName":fighteraname}, {"fighterCode":0}).distinct('fighterCode')
                afightercode = xox[0]
                winnerpage = 'https://www.fightstats.xyz/fighterdata/' + afightercode
            else:
                winnerpage = 'https://www.fightstats.xyz/fighter/' + fighteraname.strip()
                
            #Does fighter b have a fighter data page or fighter page
            query = {"fighterName": fighterbname}
            result = webfighterdata.find_one(query)
            if result:
                #Get fighter code
                xox = db.WEBFighterData.find({"fighterName":fighterbname}, {"fighterCode":0}).distinct('fighterCode')
                bfightercode = xox[0]
                loserpage = 'https://www.fightstats.xyz/fighterdata/' + bfightercode
            else:
                loserpage = 'https://www.fightstats.xyz/fighter/' + fighterbname.strip()
            
            try:
                formatted_date = new_date_string[:new_date_string.index('-')]
                new_date_string = formatted_date
            except:
                new_date_string = new_date_string
            
            fighteraname = fighteraname.strip()
            fighterbname = fighterbname.strip()
            
            fighteraname = unidecode(fighteraname)
            fighterbname = unidecode(fighterbname)
            
            fighteraname = fighteraname.replace('(C)', '')
            fighterbname = fighterbname.replace('(C)', '')
            
            mydict = {
                "Winner": fighteraname,
                "WinnerPage": winnerpage,
                "Loser": fighterbname,
                "LoserPage": loserpage,
                "Contains": fighteraname + " " + fighterbname,
                "WinnerTotalStrikes": '',
                "LoserTotalStrikes": '',
                "WinnerTD": '',
                "LoserTD": '',
                "FightPage": '',
                "LabelText": "No Data",
                "Date": new_date_string,
                "Rounds": fightround,
                "Result": fightmethod,
                
    }
            webnodatafights.insert_one(mydict) 
      
        integer_value = integer_value - 1
        

    

import requests
from bs4 import BeautifulSoup
from datetime import datetime

import pymongo

#Setting Up The Connections To The DB
myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@octc1.d2he2mx.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]

webeventdata = db["WEBEventData"]
webfightdata = db["WEBFighterFights"]

# Set the URL of the Wikipedia page
wiki_url = 'https://en.wikipedia.org/wiki/List_of_UFC_events'

# Send a GET request to the Wikipedia page
response = requests.get(wiki_url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table of past events by its ID
past_events_table = soup.find('table', {'id': 'Past_events'})

# Find all the links in the second column of the table
links = past_events_table.select('td:nth-child(2) a')

# Loop through the event links and scrape data for each event
for i, link in enumerate(links[:299]):
    fightnum = 0
    href = link['href']
    event_url = f'https://en.wikipedia.org{href}'
    
    # Send a GET request to the event page
    event_response = requests.get(event_url)

    # Parse the HTML code using BeautifulSoup
    event_soup = BeautifulSoup(event_response.content, "html.parser")

    # Extract event info
    event_name = event_soup.select_one("#mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(1) > th").text.strip()
    promotion_name = event_soup.select_one("#mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(4) > td > a").text.strip()
    date = event_soup.select_one("#mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(5) > td").text.strip()
    venue = event_soup.select_one("#mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(6) > td > a").text.strip()
    location = event_soup.select_one("#mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(7) > td > a").text.strip()

    
    
    
    output_name = event_name.replace('.', '').replace(':', '')
    
    
    mydict = {
            "eventName": output_name,
            "promotionName": promotion_name,
            "date": date,
            "venue": venue,
            "location": location,   
            }
    webeventdata.insert_one(mydict)
    
    

    
    # Find the rows with the fight data
    rows = event_soup.select("#mw-content-text > div.mw-parser-output > table.toccolours > tbody > tr")[1:]

    # Loop through the rows and extract the data for each fight
    for row in rows:
        # Extract the columns from the row
        cols = row.find_all("td")

        # Check if the row has at least 6 columns
        if len(cols) >= 6:
            # Extract the data from the columns
            weight_class = cols[0].text.strip()
            winner = cols[1].text.strip()
            loser = cols[3].text.strip()
            method = cols[4].text.strip()
            round = cols[5].text.strip()
            time = cols[6].text.strip()

            if 'No Contest' in method:
                newmethod = 'No contest'
            else:
                newmethod = method.split()[0]
            
            #Adds to the doc with each fight
            
            # Define the filter to identify the document to be updated
            filter = {"eventName": output_name}

            #sets vars
            webfightwinner = 'fight' + str(fightnum) + 'WINNER'
            webfightloser = 'fight' + str(fightnum) + 'LOSER'
            webfightmethod = 'fight' + str(fightnum) + 'METHOD'
            webfightround = 'fight' + str(fightnum) + 'ROUND'
            webfighttime = 'fight' + str(fightnum) + 'TIME'
            webfightwc = 'fight' + str(fightnum) + 'WC'
            
            webfighteralink = 'fight' + str(fightnum) + 'aLink'
            webfighterblink = 'fight' + str(fightnum) + 'bLink'
            alink = 'https://www.fightstats.xyz/search?q=' + winner + ' Profile'
            blink = 'https://www.fightstats.xyz/search?q=' + loser + ' Profile'
            
            # add all the fight data
            update = {"$set": {webfightwinner: winner }}
            webeventdata.update_one(filter, update)   
            
            update = {"$set": {webfightloser: loser }}
            webeventdata.update_one(filter, update)   
            
            update = {"$set": {webfightmethod: newmethod }}
            webeventdata.update_one(filter, update)  
            
            update = {"$set": {webfightround: round }}
            webeventdata.update_one(filter, update)  
            
            update = {"$set": {webfighttime: time }}
            webeventdata.update_one(filter, update)  
            
            update = {"$set": {webfightwc: weight_class }}
            webeventdata.update_one(filter, update) 
            
            update = {"$set": {webfighteralink: alink }}
            webeventdata.update_one(filter, update)    
            
            update = {"$set": {webfighterblink: blink }}
            webeventdata.update_one(filter, update)   
            
            update = {"$set": {'fightPage': '' }}
            webeventdata.update_one(filter, update)   
        
        
        
        
        
        
        
        
        
        
            filtera = {"fighterName": winner}
            filterb = {"fighterName": loser}
            
            
            update = {"$set": {'fightPage': '' }}
            webfightdata.update_one(filtera, update) 
            webfightdata.update_one(filterb, update) 
            
            update = {"$set": {'opponent': loser }}
            webfightdata.update_one(filtera, update) 
            
            update = {"$set": {'opponent': winner }}
            webfightdata.update_one(filterb, update) 
            
            update = {"$set": {'eventName': output_name }}
            webfightdata.update_one(filtera, update) 
            webfightdata.update_one(filterb, update) 
            
            
            
            
          
            
            
            
            
            
            
            
            
            fightnum = fightnum + 1
            
            

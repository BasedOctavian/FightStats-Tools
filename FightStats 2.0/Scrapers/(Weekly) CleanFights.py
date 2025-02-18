#Figures out the average stats per each weight class 
import pymongo
import re
import csv
import sqlite3
import random

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



# find all fights that have stats (i.e. are "tracked")
tracked_fights = webnodatafights.find({"WinnerTotalStrikes": { "$ne": ""} })

# loop through each tracked fight
for tracked_fight in tracked_fights:
    # get the loser and date of the tracked fight
    loser = tracked_fight["Loser"]
    date = tracked_fight["Date"]
     # find all fights with the same loser and date, but no stats (i.e. are "not tracked")
    non_tracked_fights = webnodatafights.find({ "Loser": loser, "Date": date, "WinnerTotalStrikes": "" })
    # loop through each "not tracked" fight and delete it
    for non_tracked_fight in non_tracked_fights:
        webnodatafights.delete_one({ "_id": non_tracked_fight["_id"] })
        
        
# loop through each tracked fight
for tracked_fight in tracked_fights:
    # get the loser and date of the tracked fight
    date = tracked_fight["Date"]
     # find all fights with the same loser and date, but no stats (i.e. are "not tracked")
     
    # set the range for the desired dates
    start_date = date - datetime.timedelta(days=2)
    end_date = date + datetime.timedelta(days=2)

    # find non-tracked fights within the date range
    non_tracked_fights = webnodatafights.find({
    "Date": {"$gte": start_date, "$lte": end_date},
    "WinnerTotalStrikes": ""
    }) 
     
    # loop through each "not tracked" fight and delete it
    for non_tracked_fight in non_tracked_fights:
        webnodatafights.delete_one({ "_id": non_tracked_fight["_id"] })
#Figures out the average stats per each weight class 
import pymongo
import csv
import sqlite3
import openai
import pyttsx3
import time

openai.api_key = "key"


#Sets Up The Voice
def speak(message):
    engine = pyttsx3.init()
    # Set the voice ID to the Microsoft Hazel voice on Windows
    engine.setProperty('voice', 'english_rp+f3')
    engine.say(message)
    engine.runAndWait()
engine = pyttsx3.init()  # object creation
voices = engine.getProperty('voices')  # getting details of current voice
#engine.setProperty('voice', voices[0].id)  # changing index, changes voices. 0 for male
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
engine.runAndWait()

presplit = str()
  
#Function for prompting gpt
def call(input):
    prompt = input
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )
    message = response.choices[0].text.strip()
    presplit = message


#Example on how to prompt gpt
#call("Who is Josh Allen")



#Setting Up The Connections To The DB
myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@octc1.d2he2mx.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]
fighterdata = db["FighterData"]
fighternames = db["FighterNames"]
weightclasses = db["WeightClasses"]
wcav = db["WCAV"]
webfighterdata = db["WEBFighterData"]


allfightsset = set()

#Filter Arguments For Each Weight Class
allfightercodes = db.WEBFighterData.distinct('fighterCode')

counter = 0

for y in allfightercodes:
    fightcode = y
    
    print(y)

    fighterDoc = db.WEBFighterData.find({"fighterCode":y})
    fighterDoc = str(fighterDoc)
    
    
    prompt = '  in a short bullet format include stats of the fighter in under 280 characters. Make sure that the stats are only pulled from the JSON style document:  ' + fighterDoc
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )
    message = response.choices[0].text.strip()
    presplit = message
    
    print(presplit)
    call(presplit)
    
    counter = counter + 1
    
    
    if counter > 5:
        print('itsover')
        time.sleep(10)
        exit
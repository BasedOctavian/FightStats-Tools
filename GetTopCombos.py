import pymongo
import collections as ct 

#Setting Up The Connections To The DB
myclient = pymongo.MongoClient("mongodb+srv://FightStatsAdmin:FightStatsAdmin716@cluster0.hufkz1t.mongodb.net/?retryWrites=true&w=majority")
db = myclient["FightStatsDB"]
combos = db["Combinations"]


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

l = db.Combinations
fightsTracked = l[0]

x = l.find({"fighterCode":y},{"_id":0})

docstring = str()
split1 = list()
absorbed = list()

landed = list()




for document in x:
    #print(document)
    docstring = str(document)
    docstring = docstring.replace(',', '')
    docstring = docstring.replace(':', '')
    docstring = docstring.replace('}', '')
    split1 = docstring.split(",")
    split2 = docstring.split("'")

    split2.remove(y)
    split2.remove("fighterCode")
    split2.remove("{")
    
    while (' ' in split2):
        split2.remove(' ')
    
    for x in split2:
        x.replace(" ", "")
        x.replace("ABS", "")

    

    
    dd = ct.defaultdict(int)
    iterable = iter(split2)
    for word in iterable:
        dd[word] += int(next(iterable)) 
    
    for k in list(dd.keys()):
        if k.startswith('ABS'):
            del dd[k]
            
    for k in list(dd.keys()):
        if k.startswith('_'):
            dacount = k.count("_")
            if dacount < 2:
                del dd[k]
    
    sortedDD = sorted(dd.items(), key=lambda x:x[1])
    
    for o in sortedDD:
        count = o.count('_')
        if count == 1:
            sortedDD.remove(o)
    
    for x in sortedDD:
        print(x)
        
cagepositions = dict()

l = db.FighterData.find({"fighterCode":y},{"CenterOctagon":1,  "_id":0}).distinct('CenterOctagon')
cagepositions.update({"CenterOctagon": l[0]})

l = db.FighterData.find({"fighterCode":y},{"PushedBackToCage":1,  "_id":0}).distinct('PushedBackToCage')
cagepositions.update({"PushedBackToCage": l[0]})

l = db.FighterData.find({"fighterCode":y},{"PushingAgainstCage":1,  "_id":0}).distinct('PushingAgainstCage')
cagepositions.update({"PushingAgainstCage": l[0]})

l = db.FighterData.find({"fighterCode":y},{"OnTopGround":1,  "_id":0}).distinct('OnTopGround')
cagepositions.update({"OnTopGround": l[0]})

l = db.FighterData.find({"fighterCode":y},{"OnBottomGround":1,  "_id":0}).distinct('OnBottomGround')
cagepositions.update({"OnBottomGround": l[0]})

l = db.FighterData.find({"fighterCode":y},{"InClinch":1,  "_id":0}).distinct('InClinch')
cagepositions.update({"InClinch": l[0]})

l = db.FighterData.find({"fighterCode":y},{"BeingClinched":1,  "_id":0}).distinct('BeingClinched')
cagepositions.update({"BeingClinched": l[0]})

l = db.FighterData.find({"fighterCode":y},{"TotalPositionPoints":1,  "_id":0}).distinct('TotalPositionPoints')
TotalPositionPoints = int()
TotalPositionPoints = l[0]

sortedPOS = list()


sortedPOS = sorted(cagepositions.items(), key=lambda x:x[1])



print("//////////////////////////////////")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("//////////////////////////////////")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("//////////////////////////////////")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

print("Cage Positions: ")


if TotalPositionPoints < 2:
    print("Not Enough Data")
else:
    for x in sortedPOS:
        print(x)





input("Press Any Key To Exit")
SystemExit
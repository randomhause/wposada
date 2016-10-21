#session13

import random

ROSTER = {"Beshansky": 0, 
          "Collins": 0,
          "Fischer": 1,
          "Giovanucci": 0,
          "Jain": 0,
          "Kim": 0,
          "Lauture": 0,
          "Lee": 0,
          "Maddox": 0,
          "Martinez": 0,
          "Mendez": 0,
          "Oh": 0,
          "Petrone": 1,
          "Posada": 0,
          "Rule": 1,
          "Schilb": 0,
          "Tariq": 0,
          "Wang": 0,
          "Wolf": 0}

'''key:value'''

def call(roster):
    '''  Among the names that are called least times,
    print one name
    roster: a dict of names and integers

    TO-DO: update dict after every call
    TO-DO: 
    '''
    #SUDO Code
    #creating a subset list with value in min in dict
    #min(roster,key=roster.values)
        #min(iterable,[, key, default])
    #random.choice(temp)
#first soluiton 
    temp_list = roster.values() #all # in roster
    min_value = min(temp_list)

    tem_dict = dict() #or {} #list()
    for key, value in roster.items(): #travel a dic with this, not indexed need to iterate thorugh list. items return thems in pairs two per pair. 
        if value == min_value: 
            #key.append(key) #key = name #how you do it to a list
            temp_dict[key] = value #add new key to a dict 
    #we have a list of names that haven't been called before

    return random.choice(temp_dict.keys())

#Second solution
    value_list = roster.values()
    min_value = min(value_list)

    names = []
    for name, number in roster.items():
        if number == min_value:
            names.append(name)

    return random.choice(names)


print(call(ROSTER))
print(call(ROSTER))
print(call(ROSTER))

#3rd Logic
db = dbm.open('db_student', 'c')

for student in ROSTER: 
    db[student] = (key)
    

    
    #print(random.sample(roster,3))
call(ROSTER)
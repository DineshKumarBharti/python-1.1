
# Dictionary 
person={
    "Name":"dinesh",
    "age": 20 ,
    "city":"satna",
    "address": "mp satna",
    "age":48,
    "city": "pune",
    "loc":"pune",
    "skill":["html","java","python","c++"]

}
# print(person["skill"][2])

# for i in person:
    # print(person[i])

# print(type(person["skill"]))

# print(person.get("loc"))
# print(person.keys())
# print(person.values())
# print(person.items())
person["Name"]="umesh"  # update karega value ko
person["age"]= 5          #  new wali  value update karega 

# print(person.items())  
     # update karega value ko print karega  dict_items([('Name', 'umesh'), ('age', 5), ('city', 'pune'), ('address', 'mp satna'), ('loc', 'pune'), ('skill', ['html', 'java', 'python', 'c++'])])

# for x,y in person.items():
    # print(x,y)

# Name umesh
# age 5
# city pune
# address mp satna
# loc pune
# skill ['html', 'java', 'python', 'c++']

# person.update({"year":2023})
# print(person)
# 'year':2023

person.pop("Name")   # delete kar dega --   key: value   ---- dono ko
person.popitem()   # list ko only delete karega

#person.clear() #  {} ye rahega but dict ka all item delete ho jayegea
#del person    # all delete 

newdict=person.copy()
# print(newdict)

# {'age': 5, 'city': 'pune', 'address': 'mp satna', 'loc': 'pune'}

Students={
    "Sanjay": {
        "math":67,
        "hindi":70,
        "english":80
    },
    "Rajeev":{
         "math":50,
        "hindi":40,
        "english":90
    },
 "Dinesh":{
        "math":65,
        "hindi":72,
        "english":85
}
}
# print(Students ["Sanjay"])
# print(Students ["Sanjay"] ["hindi"])

# for x in Students:
    # print(Students[x])

# {'math': 67, 'hindi': 70, 'english': 80}
# {'math': 50, 'hindi': 40, 'english': 90}
# {'math': 65, 'hindi': 72, 'english': 85}

# for x in Students.values():
    # print(x)
# {'math': 67, 'hindi': 70, 'english': 80}
# {'math': 50, 'hindi': 40, 'english': 90}
# {'math': 65, 'hindi': 72, 'english': 85}

for x in Students.values():
    for y in x:
        print(y,"      ",end="")
    print()

# math       hindi       english
# math       hindi       english
# math       hindi       english


for x in Students:
    print(x,":" , end=" ")
    for y in Students[x].values():
        print(y,end="    ")
    print()

# Sanjay : 67    70    80
# Rajeev : 50    40    90
# Dinesh : 65    72    85

for x in Students.values():
    for y in x.values():
        print(y,end="  ")
#  67  70  80  50  40  90  65  72  85

for x in Students.values():
    for y in x.values():
        print(y,"  ",end="  ")
    print()
# 50     40     90
# 65     72     85
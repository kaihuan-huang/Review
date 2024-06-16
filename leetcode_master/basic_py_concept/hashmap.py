# HashMap(aka dic) 
# cannot have duplicae keys inside the Hash Map {}
myMap = {}
myMap["justin"] = 88
myMap["Ines"] = 77
print(myMap) #key value pair {'justin': 88, 'Ines': 77}
print(len(myMap))

myMap["justin"] = 566
print(myMap["justin"])

#search if a key exists in a hashmap in constant time, and remove a key
print("justin in myMap","justin" in myMap)
myMap.pop("justin")
print("justin" in myMap)

#to initialze a hashmap{}
myMap = { "Ace" : 99, "Bob" : 88}
print(myMap)

# Dict comprehension use most while dong graph problems: build an adjacency list
myMap = { i: 2*i for i in range(8) }
print(myMap) #{0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14}

#Looping through maps
myMap = { "jusitn": 11, "Bob": 22 }
for key in myMap:
    print('key',key,"myMap[key]", myMap[key])
    
for val in myMap.values():
    print("val", val)
    
for key, val in myMap.items():
    print("key", key, "val", val)
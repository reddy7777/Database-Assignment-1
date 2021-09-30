import pymongo
from pymongo import MongoClient
con = MongoClient("mongodb+srv://root:Aishu@cluster0.kkrqm.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
print(con)
database = con['databaseassignment']
collection = database['studentmarks']
name = input("enter name:")
Id = input("enter id:")
m1 = int(input("enter marks1:"))
m2 = int(input("enter marks2:"))
m3 = int(input("enter marks3:"))
m4 = int(input("enter marks4:"))
m5 = int(input("enter marks5:"))
total = (m1+m2+m3+m4+m5)
avg = total/5
dic = {
    "name" : name,
    "ID" : Id,
    "mark1": m1,
    "mark2" : m2,
    "mark3" : m3,
    "mark4" : m4,
    "mark5" : m5,
    "total" : total,
    "average" : avg
}
print(dic)
collection.insert_one(dic)
result = collection.find({})
for res in result:
    print(res)
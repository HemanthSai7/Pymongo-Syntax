import json
from pymongo import MongoClient
from DBConnection import Singleton
client = MongoClient(uri)

mydb=client["LearnMongoDB"]
mycol=mydb["collection1"]

#inserting records


# dataset1=json.dumps(dataset1)
# print(json.loads(dataset1))

"""insert records"""
# mycol.insert_many(dataset1)

"""count dcouments in collection"""
# print(mycol.count_documents({}))

"""find documents"""
# for doc in mycol.find({}):
#   print(doc)

"""$and"""
# for doc in mycol.find({
#   "$and":[
#     {
#       "capital":"Washington, D.C.",
#     },
#     {
#       "name":"United States",
#     }
#   ]
# }):
#   # doc=json.dumps(doc)
#   print(doc)

"""$or"""
# for doc in mycol.find({
#   "$or":[
#     {
#       "capital":"Washington, D.C.",
#     },
#     {
#       "capital":"Canberra",
#     }
#   ]
# }):
#   print(doc)

"""$in"""
# for doc in mycol.find({
#   "$or":[
#     {
#     "capital":"Washington, D.C."
#     },
#     {
#       "population":{
#         "$in":[
#           125960000,
#           210147125
#         ]
#       }
#     }
#   ]
# }):
#   print(doc)

"""$lt"""
# for doc in mycol.find({
#   "$or":[
#     {
#       "population":{
#         "$lt":328239523
#       }
#     },
#     {
#       "population":{
#         "$in":[
#           125960000,
#           210147125
#         ]
#     }
#     }
#   ]
# }):
#   print(doc)

"""$gt"""
for doc in mycol.find({
  "$or":[
    {
      "population":{
        "$gt":328239523
      }
    },
    {
      "population":{
        "$in":[
          125960000,
          210147125
        ]
    }
    }
  ]
}):
  print(doc)

"""$eq""" 
# for doc in mycol.find({
#   "$or":[
#     {
#       "name":{
#         "$eq":"Australia"
#       }
#     },
#     {
#       "population":{
#         "$in":[
#           125960000,
#           210147125
#         ]
#     }
#     }
#   ]
# }):
#   print(doc)

"""$ne"""
# for doc in mycol.find({
#   "$or":[
#     {
#       "name":{
#         "$eq":"Australia"
#       }
#     },
#     {
#       "name":{
#         "$ne":"United States"
#       }
#     }
#   ]
# }):
#   print(doc)

"""$nin"""

for doc in mycol.find({
  "$or":[
    {
      "capital":"Washington, D.C.",
    },
    {
      "population":{
        "$nin":[
          125960000,
          210147125
        ]
    }
    }
  ]
}):
  print(doc)

